from .models import db , Package , Booking,User,Role
from flask import current_app as app
from datetime import datetime
with app.app_context():
    db.create_all()
    ds = app.security.datastore
    ds.find_or_create_role(name = "admin" ,  desc="superuser")
    ds.find_or_create_role(name="professional" , desc="serviceprovider")
    ds.find_or_create_role(name="customer" , desc="user")
    db.session.commit()

    if not ds.find_user(email="admin@gmail.com"):
        ds.create_user(name="himanshu" , email="admin@gmail.com" , password = "pass" , roles=["admin"  ])
        db.session.commit()
    if not ds.find_user(email="prof1@gmail.com"):
        ds.create_user(name="prof1" , email="prof1@gmail.com" , password = "pass" , roles=["professional"  ])
        db.session.commit()
    if not ds.find_user(email="prof2@gmail.com"):
        ds.create_user(name="prof2" , email="prof2@gmail.com" , password = "pass" , roles=["professional"  ])
        db.session.commit()
    if not ds.find_user(email="cust1@gmail.com"):
        ds.create_user(name="cust1" , email="cust1@gmail.com" , password = "pass" , roles=["customer"  ])
        db.session.commit()
    if not ds.find_user(email="cust2@gmail.com"):
        ds.create_user(name="cust2" , email="cust2@gmail.com" , password = "pass" , roles=["customer"  ])
        db.session.commit()

    if Package.query.count() == 0:
        pack1 = Package(name = "Past Control" , price= 500 , status="Open" , professional_id=2)
        pack2 = Package(name = "Sofa Cleaning" , price= 500 , status="Open" , professional_id=2)
        pack3 = Package(name = "Gardening" , price= 500 , status="Open" , professional_id=3)
        pack4 = Package(name = "Weed Removal" , price= 500 , status="Open" , professional_id=3)
        db.session.add_all([pack1,pack2,pack3,pack4])
        db.session.commit()

    if Booking.query.count() == 0:
        book1 = Booking(date = datetime.strptime("25-06-2024" , "%d-%m-%Y").date(),
                        time = datetime.strptime("11:30" , "%H:%M").time() ,
                        customer_id  = 4 , professional_id=2 , package_id =1)
        book2 = Booking(date = datetime.strptime("25-06-2024" , "%d-%m-%Y").date(),
                        time = datetime.strptime("11:30" , "%H:%M").time() ,
                        customer_id  = 4 , professional_id=3 , package_id =4)
        book3= Booking(date = datetime.strptime("25-06-2024" , "%d-%m-%Y").date(),
                        time = datetime.strptime("11:30" , "%H:%M").time() ,
                        customer_id  = 5 , professional_id=2 , package_id =2)
        book4= Booking(date = datetime.strptime("25-06-2024" , "%d-%m-%Y").date(),
                        time = datetime.strptime("11:30" , "%H:%M").time() ,
                        customer_id  = 5 , professional_id=3 , package_id =3)
        db.session.add_all([book1, book2,book3,book4])
        db.session.commit()
        

    # prof2 = User.query.filter_by(email="prof2@gmail.com").first()
    # print(prof2.name)
    # print(prof2.id)
    # print(prof2.recived_bookings)
    # print(prof2.recived_bookings[0].customer_id)


    # pack = Package.query.filter_by(id=2).first()
    # print(pack.bookings)
    # booking3 =  Booking.query.filter_by(id=3).first()
    # print(booking3.professional_id)
    # print(booking3.professional)
    # print(booking3.professional.id)
    # print(booking3.professional.name)
    # print(booking3.package.name)


    