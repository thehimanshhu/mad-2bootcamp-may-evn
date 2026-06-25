from flask import current_app as app
from .models import db, User, Package, Booking, Role
from flask import request
from flask_security import auth_required, roles_required
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


@app.route("/prof-greet", methods=["GET"])
def prof_dashboard():
    return {"message" : "welcome to Prof dashboard"}