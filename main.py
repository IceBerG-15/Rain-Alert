import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv(".\projects\\rain_alert\\.env") 


#twilio settings
my_twilio_no=os.getenv('TWILIO_NO')

account_sid=os.getenv('ACCOUNT_SID')
auth_token=os.getenv('AUTH_TOKEN')

#name of place--- Kharagpur
my_lat=22.339430
my_long=87.325340
api_key=os.getenv('API_KEY')
api_link=f'https://api.openweathermap.org/data/2.5/onecall?lat={my_lat}&lon={my_long}&exclude="current,minutely,daily"&appid={api_key}'
will_rain=False
response = requests.get(api_link)
data=response.json()
hourly_data=data['hourly'][0:12]
for hour in hourly_data:
    condition=hour['weather'][0]['id']
    if condition<700:
        will_rain=True


if will_rain:
    client=Client(account_sid,auth_token)
    message = client.messages \
            .create(
                    body="Its going to rain today. bring your umbrella ☂️",
                    from_=my_twilio_no,
                    to=os.getenv('TO_NUMBER')
                )

    print(message.sid)








