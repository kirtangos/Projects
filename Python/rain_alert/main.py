

import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_id="6798a5a52ec8adc63b50fbf0f9be52f4"
account_sid = "AC80e61ed7383dd2c69febab5967d16e75"
auth_token = "7838693c2a45204b6c7102b904616016"


weather_params={
    "lat": 3.790000,
    "lon": 125.608000,
    "appid" : api_id,
    "cnt": 4,

}

response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
 
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code) < 700 :
        will_rain=True
if will_rain:
    client=Client(account_sid,auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember to bring an umbrella.", 
        from_='+18459578831',
        to='+919960652844'
    )
    print(message.status)



   