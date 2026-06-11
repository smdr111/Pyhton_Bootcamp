import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
        self.verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")
        awlf.client = Client(self.account_sid, self.auth_token)
    def send_whatsapp(self,message):    
        news = self.client.messages.create(
            body=message,
            from_=f"whatsapp:{self.whatsapp_number}",
            to=f"whatsapp:{self.verified_number}"
        )
        return news.sid




