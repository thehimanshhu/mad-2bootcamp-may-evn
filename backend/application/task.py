from celery import shared_task
import time
from .models import db, User , Booking
import csv

@shared_task(name = "addnumbers" ,ignore_result=False)
def add_together(a , b) -> int:
    time.sleep(20)
    return a + b


@shared_task(name = "export_csv" , ignore_result=False)
def export_csv(cust_id):
    time.sleep(10)
    bookings = db.session.query(Booking).filter_by(customer_id = cust_id).all()

    filename= f"customer-{cust_id}.csv"
    with open("./static/" + filename , "w") as csv_file:
        csv_obj = csv.writer(csv_file , delimiter=",")
        csv_obj.writerow(["No." , "Package Name" , "Professional Name" , 
                          "Professional Email" , "Date" , "Time"])
        for index,booking  in  enumerate(bookings):
            csv_obj.writerow([index+1  , booking.package.name , booking.professional.name, booking.professional.email,
                              booking.date, booking.time])
        
    return filename
from datetime import datetime

from .utils import preare_tmp
from .mail import send_email

@shared_task(name = "admin_monthly_report" , ignore_result=True)
def admin_report():
    start_date = datetime.strptime("01-06-2026" ,"%d-%m-%Y").date()
    end_date= datetime.strptime("30-06-2026" ,"%d-%m-%Y").date()

    bookings = db.session.query(Booking).filter(Booking.date.between(start_date,end_date)).all()
    output = preare_tmp("./templates/admin-export-mail.html" , data= {"username" : "Admin" , "bookings" : bookings})
    send_email("admin@gmail.com" , "Monthly Activity Report for Jun 2026" , output)
    return "Done"