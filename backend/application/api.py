from flask import current_app as app
from .models import db, User, Package, Booking, Role
from flask import request
from flask_security import auth_required, roles_required , current_user
from datetime import datetime
@app.route("/")
def home():
    return "Hello"

@app.route("/login" , methods=["POST"])
def login():
    email = request.json.get("email")
    pwd = request.json.get("pass")
    
    role = request.json.get("role")
    user = User.query.filter_by(email=email).first() 
    if user:
        if user.password ==pwd : 
            return {"message" : "Login Successful! " ,
                    "role" : user.roles[0].name , "token" : user.get_auth_token() }
        else:
            return {"message" : "Incorrect password"} , 401
    else:
        return {"message" : "Email doesn't exist"} , 404


@app.route("/register" , methods=["POST"]) 
def register():
    email = request.json.get("email")
    pwd = request.json.get("password")
    role = request.json.get("role")
    print(role)
    name = request.json.get("name") 
    ds = app.security.datastore
    
    if not ds.find_user(email = email):
        
        if role == "customer": 
            ds.create_user(email = email , password = pwd, name= name , active= "active" , roles=["customer"])
            db.session.commit()
            return {"message" : "Account created Successfully"} , 200
        elif role == "professional": 
            ds.create_user(email = email , password = pwd, name= name , active= "active" , roles=["professional"])
            db.session.commit()
            return {"message" : "Account created Successfully"} , 200  
        else :
            
            return {"message" : "Role not Allowed"} , 400
    else:
        
        return { "message" : "Email Already Exists"} , 409
        
@app.route("/admin/dashboard", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_dashboard():
    return {"message" : "welcome to admin dashboard"}





@app.route("/list-professionals" , methods=["GET"])
@auth_required("token")
@roles_required("admin")
def list_professionals():
    prof_role = Role.query.filter_by(name = "professional").first()
    profs = []
    for prof in prof_role.bearers:
        profs.append({ "id" : prof.id , "name" : prof.name , "email" : prof.email})
    return profs


@app.route("/list-customers" , methods=["GET"])
@auth_required("token")
@roles_required("admin")
def list_customers():
    cust_role = Role.query.filter_by(name = "customer").first()
    custs = []
    for cust in cust_role.bearers:
        custs.append({ "id" : cust.id , "name" : cust.name , "email" : cust.email})
    return custs


@app.route("/list-packages" , methods=["GET"])
@auth_required("token")
@roles_required("professional")
def list_packages():
    packages = Package.query.filter_by(professional_id = current_user.id).all()
    packs = []
    for pack in packages:
        packs.append({"name" :pack.name , "price" : pack.price , "id" : pack.id})
    return packs , 200


@app.route("/create-package" , methods=["POST"])
@auth_required("token")
@roles_required("professional")
def create_package():
    name = request.json.get("name")
    price = request.json.get("price")
    print(name)
    print(price)
    if name and price : 
        new_pack = Package(name= name , price= price , professional_id = current_user.id ,status="Open" )
        db.session.add(new_pack)
        db.session.commit()
        return {"message" :"Package Created Successfully" },200
    else : 
        return {"message" : "name or price can't be empty" }  , 400
    

@app.route("/get-package" , methods=["GET"])
@auth_required("token")
def get_package():
    pack_id = request.args.get("pack_id")
    pack = Package.query.filter_by(id = pack_id).first()
    if pack:
        package = {}
        package["name"] = pack.name
        package["price"] = pack.price
        package["bookings"] = []
        for booking in pack.bookings:
            package["bookings"].append( { "id" : booking.id, "customer_name" : booking.customer.name,
                                        "customer_email" : booking.customer.email ,
                                        "date" : datetime.strftime(booking.date , "%d-%m-%Y" ) , 
                                        "time" : booking.time.strftime("%H:%M")  })
        return package , 200
    else :
        return {"message":"Package Not found"},404
