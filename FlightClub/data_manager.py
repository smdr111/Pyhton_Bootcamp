import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price_endpoint = os.getenv("SHEETY_PRICE_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.token = os.getenv("SHEETY_TOKEN")
        response = requests.get(url=self.price_endpoint,headers={"Authorization": f"Basic {self.token}"})
        response.raise_for_status()
        self.price_data = response.json()['prices']

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers={"Authorization": f"Basic {self.token}"})
        response.raise_for_status()
        user_emails = response.json()
        return user_emails['users']


    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self.price_endpoint}/{row_id}",
            json=new_data,
            headers={"Authorization": f"Basic {self.token}"}
        )


data_m = DataManager()
data = data_m.get_customer_emails()
print(data)