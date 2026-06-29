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