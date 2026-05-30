import requests
from twilio.rest import Client
WEATHER_EP = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API = "YOUR WEATHER API KEY"
account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"

parameters = {
    'lat':38.715523,
    'lon':-75.081788,
    'appid':WEATHER_API,
    'cnt':4,
}

response = requests.get(WEATHER_EP,params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hourly_weather in weather_data['list']:
    if hourly_weather['weather'][0]['id']< 700:
        will_rain =True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember bring an ☔️",
        from_="+18775474718",
        to="+13023639954",
    )
    print(message.status)

