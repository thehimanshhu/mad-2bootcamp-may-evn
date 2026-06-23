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

        
@app.route("/admin/dashboard", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def admin_dashboard():
    return "Welcome to admin dashboard"