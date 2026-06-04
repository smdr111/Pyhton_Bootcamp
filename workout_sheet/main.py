import requests
from datetime import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 173
AGE = 22

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
NUTRITION_ENDPOINT = os.getenv("NUTRITION_ENDPOINT")

NUTRITION_HEADERS = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
SHEETY_HEADER = {
    "Authorization":f"Bearer {SHEETY_AUTH_TOKEN}"
}

exercise_text = input('Tell me which exercises you did: ')
user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

n_response = requests.post(url=NUTRITION_ENDPOINT,json=user_params,headers=NUTRITION_HEADERS)
data = n_response.json()

today = dt.now().strftime("%m/%d/%Y")
time = dt.now().strftime("%X")

for item in data['exercises']:
    sheety_params = {
        'workout':{
            'date':today,
            'time':time,
            'exercise':item['name'].title(),
            'duration':item['duration_min'],
            'calories':item['nf_calories']
        }
    }

sheet_r = requests.post(url=SHEETY_ENDPOINT,json=sheety_params,headers=SHEETY_HEADER)
sheet_r.raise_for_status()



















