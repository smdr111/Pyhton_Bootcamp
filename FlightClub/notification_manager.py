import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
        self.verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)
        self.my_email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
        self.connection = smtplib.SMTP(os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS"),port=587)

    def send_whatsapp(self,message):
        news = self.client.messages.create(
            from_ = f"whatsapp:{self.whatsapp_number}",
            body = message,
            to=f"whatsapp:{self.verified_number}"
        )
        return news.sid
    def send_email(self,email_list,message):
            with self.connection:
                self.connection.starttls()
                self.connection.login(user=self.my_email, password=self.password)
                for email in email_list:
                    self.connection.sendmail(from_addr=self.my_email,
                                        to_addrs=email,
                                        msg=message)




