import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.getenv("SHEETY_ENDPOINT")
        self.token = os.getenv("SHEETY_TOKEN")
        response = requests.get(url=self.endpoint,headers={"Authorization": f"Basic {self.token}"})
        response.raise_for_status()
        self.data = response.json()['prices']

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self.endpoint}/{row_id}",
            json=new_data,
            headers={"Authorization": f"Basic {self.token}"}
        )

