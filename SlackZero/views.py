from django.http import HttpResponse
from django.shortcuts import render

import json
import requests

# url = "https://api.zerobounce.net/v2/validate"
# api_key = "3d728439c77f43e1b41a9dabc446fd3c"
# email = "ethanasfasdfsa@clearbanc.com"
# ip_address = "99.123.12.122" #ip_address can be blank
# params = {"email": email, "api_key": api_key, "ip_address": ip_address}
# response = requests.get(url, params=params)
# data = response.json()
# resp1 = data["status"]

#resp1 = json.loads(response.content)
#resp1 = response.text

# Print the returned json
#print (resp1)

thread = None

def verify_email(request):
    # global thread
    # thread = threading.Thread(target=talk_to_zerobounce, pass response_url somehow)
    # thread.start()
	return HttpResponse(json.dumps(
    {
    "response_type": "in_channel",
    "text": "It's 80 degrees right now.",
    "attachments": [
        {
            "text":"Partly cloudy today and tomorrow"
        }
    ]
    }))

# def talk_to_zerobounce():
#     send a response

# print resp1
# {
#  "address":email_to_verify,
#  "status":"valid",
#  "sub_status":"",
#  "free_email":True,
#  "did_you_mean":None,
#  "account":"flowerjill",
#  "domain":"aol.com",
#  "domain_age_days": "8426",
#  "smtp_provider":"yahoo",
#  "mx_record":"mx-aol.mail.gm0.yahoodns.net",
#  "mx_found": True,
#  "firstname":"Jill",
#  "lastname":"Stein",
#  "gender":"female",
#  "country":"United States",
#  "region":"Florida",
#  "city":"West Palm Beach",
#  "zipcode":"33401",
#  "processed_at":"2017-04-01 02:48:02.592"
# }
