from flask import current_app as app
from .models import db, User, Package, Booking, Role
from flask import request
from flask_security import auth_required, roles_required , current_user
from datetime import datetime
from app import cache
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

@app.route("/get-professional" , methods=["GET"])
@auth_required("token")
def get_professional():
    prof_id = request.args.get("prof_id")
    prof = User.query.filter_by(id = prof_id).first()
    if prof:
        professional = {}
        professional["name"] = prof.name
        professional["email"] = prof.email
        professional["packages"] = []
        for pack in prof.packages:
            professional["packages"].append( {"id" : pack.id , "name" :pack.name , "price":pack.price})

        return professional , 200
    else :
        return {"message":"Professional Not found"},404
    



@app.route("/get-packages" , methods=["GET"])
@auth_required("token")
def get_packages():
    pack_id = request.args.get("pack_id")
    packs = Package.query.all()
    packages  = []
    for pack in packs:
        packages.append({"id" : pack.id , "name" : pack.name , "price" : pack.price})
    return packages,200


@app.route("/book-package" , methods=["POST"])
@auth_required("token")
def book_package():
    p_id = request.args.get("pack_id")
    date = request.json.get("date")
    time = request.json.get("time")
    pack = Package.query.filter_by(id = p_id).first()
    if pack:
        new_booking = Booking(date = datetime.strptime(date  , "%Y-%m-%d").date() ,
                              time = datetime.strptime(time, "%H:%M").time() ,
                              customer_id = current_user.id , professional_id = pack.professional.id,
                              package_id = pack.id)
        db.session.add(new_booking)
        db.session.commit()
        return {"message" : "Booking Created Succesfully"} , 200
    else : 
        return {"message" : "Package Doesn't exist"} , 404
    

@app.route("/get-bookings" , methods=["GET"]) 
@cache.cached(1800)
@auth_required("token")
def get_bookings():
    bookings = Booking.query.filter_by(customer_id = current_user.id).all()
    books = []
    for book in bookings : 
        books.append({"id" :book.id , "prof_name" : book.professional.name , 
                      "prof_email" : book.professional.email , 
                      "date" : datetime.strftime(book.date , "%d-%m-%Y" ) , 
                        "time" : book.time.strftime("%H:%M") , 
                           "package_name"  :book.package.name })
    return books,200


@app.route("/search" , methods=["POST"])
def search():
    q_type = request.json.get("query_type")
    query  = request.json.get("query")
    if q_type== "prof":
        prof_role = Role.query.filter_by(name = "professional").first()
        profs = []
        for prof in prof_role.bearers:
            if query in prof.name.lower()  or query in prof.email.lower():
                profs.append({ "id" : prof.id , "name" : prof.name , "email" : prof.email})
        return profs , 200
    if q_type== "cust":
        cust_role = Role.query.filter_by(name = "customer").first()
        custs = []
        for cust in cust_role.bearers:
            if query in cust.name.lower()  or query in cust.email.lower():
                custs.append({ "id" : cust.id , "name" : cust.name , "email" : cust.email})
        return custs , 200


from .task import add_together , export_csv

@app.route("/add_number" , methods=["GET"])
def add_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add_together.delay(a,b)
    
    return {"task_id" : result.id}


from celery.result import AsyncResult

@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


@app.route("/export-csv" , methods=["GET"])
@auth_required("token")
@roles_required("customer")
def export_customer_csv():
    result = export_csv.delay(current_user.id)
    return {"task_id" : result.id}

from random import randint 
@app.route("/random")
@cache.cached(30)
def random():
    return str(randint(1,100))