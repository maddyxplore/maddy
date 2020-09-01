# ---------------------------seding_otp------------------------------------------#
import random # importing random module fopr otp
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def generate():
    num = random.randint(100000,999999)
    return num
sender_email = input("Enter the reciever email")
receiver_email = input("Enter the sender email")
password = input("Enter the sender password")

message = MIMEMultipart("alternative")
message["Subject"] = "OTP-BikeFeedOnline"
message["From"] = sender_email
message["To"] = receiver_email
# str to be send as mail
gen_otp = str(generate())
text = "Your otp for the Bikefeed is: "+gen_otp
part1 = MIMEText(text, "plain")
message.attach(part1)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
def check():
    otp = str(input('Enter the otp: '))
    if otp == gen_otp:print("OTP-Verified")
    else:print("OTP-Not verified")
check() #checking the OTP
# ---------------------------seding otp------------------------------------------#
