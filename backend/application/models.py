from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String , nullable = False)
    email = db.Column(db.String , unique = True ,  nullable = False)
    password = db.Column(db.String , nullable = False)
    roles = db.relationship("Role" ,secondary="user_roles" , backref="bearers")
    fs_uniquifier = db.Column(db.String, nullable=False)
    active=db.Column(db.String,nullable=False)
    packages = db.relationship("Package" , backref="professional")
    created_bookings = db.relationship("Booking" , foreign_keys="Booking.customer_id" ,backref ="customer")
    recived_bookings = db.relationship("Booking" , foreign_keys="Booking.professional_id" ,backref ="professional")
    
class Role(db.Model , RoleMixin):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String , nullable = False)
    desc = db.Column(db.String , nullable = False)

class UserRole(db.Model):
    __tablename__ ="user_roles"
    id = db.Column(db.Integer , primary_key =True)
    user_id  = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)
    role_id = db.Column(db.Integer , db.ForeignKey("role.id") , nullable = False)

class Package(db.Model):
    __tablename__ = "package"
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String , nullable = False)
    price =db.Column(db.Integer , nullable=False)
    professional_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)
    status=db.Column(db.String , nullable = False)
    bookings =db.relationship("Booking" , backref ="package" )

class Booking(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    date = db.Column(db.Date , nullable = False)
    time  = db.Column(db.Time, nullable = False)
    price =db.Column(db.Integer , nullable=True)
    customer_id =  db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)
    package_id = db.Column(db.Integer , db.ForeignKey("package.id") , nullable = False)
    professional_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)


