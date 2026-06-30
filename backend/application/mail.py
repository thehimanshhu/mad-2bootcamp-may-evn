import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
server_host = "localhost"
server_port = 1025
sender_address = "donotreply@helpify.com"
sender_password = ""

def send_email(to_address , subject , message):
    msg = MIMEMultipart()
    msg["From"] = sender_address
    msg["To"] = to_address
    msg["Subject"] = subject

    msg.attach(MIMEText( message , "html") )

    s=smtplib.SMTP(host=server_host , port = server_port)
    s.login(sender_address, sender_password)
    s.send_message(msg)
    s.quit()
    return "Mail Sent"