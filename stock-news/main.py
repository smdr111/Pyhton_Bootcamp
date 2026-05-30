import requests
from twilio.rest import Client
from datetime import date,timedelta

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

COMPANY_NAME = "Tesla"
STOCK_NAME = "TSLA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"


stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':STOCK_API_KEY,
}
r_stock = requests.get(STOCK_ENDPOINT,params=stock_params)
r_stock.raise_for_status()
stock_data = r_stock.json()

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before = str(today - timedelta(days=2))

yesterday_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
day_before_price = float(stock_data['Time Series (Daily)'][day_before]['4. close'])

diff = round((yesterday_price - day_before_price)/day_before_price * 100,2)

up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )









