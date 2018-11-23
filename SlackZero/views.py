from django.http import HttpResponse
from django.shortcuts import render
#from slackclient import SlackClient
#import os
#from threading import Thread
import json
import requests

def verify_email(request):
    print(dir(request))
    print(request.POST)
    email = request.POST['text']
    url_ZB = "https://api.zerobounce.net/v2/validate"
    api_key = "3d728439c77f43e1b41a9dabc446fd3c"
    ip_address = "99.123.12.122" #ip_address can be blank
    params_ZB = {"email": email, "api_key": api_key, "ip_address": ip_address}
    response = requests.get(url_ZB, params=params_ZB)
    data = response.json()
    resp1 = email + ' - ' + data["status"]

    url_server = "https://sheltered-sands-95126.herokuapp.com/SlackZero/verify-email"
    params_server = {"text": resp1, "response_type": "in_channel"}
    requests.post(url_server, params=params_server)
    # data = response.json()
    return HttpResponse(resp1)


# Print the returned json
#print (resp1)
# slack_client = SlackClient(os.environ.get("xoxb-4545660241-486093960406-htIW5JtsT152dcEEhHTKq9TF"))
# starterbot_id = None
# starterbot_id = slack_client.api_call("auth.test")["user_id"]
thread = None

# def verify_email(request):
#     # global thread
#     # thread = threading.Thread(target=talk_to_zerobounce, pass response_url somehow)
#     # thread.start()
#     input_value()
#     return HttpResponse(json.dumps(
#     {
#     "response_type": "in_channel",
#     "text": data["text"],
#     }))

# def talk_to_zerobounce():
#     send a response

# from threading import Thread
#
# def backgroundworker(somedata,response_url):
#
#     # your task
#
#     payload = {"text":"your task is complete",
#                 "username": "bot"}
#
#     requests.post(response_url,data=json.dumps(payload))
#
# @app.route('/appmethodaddress',methods=['POST','GET'])
# def receptionist():
#
#     response_url = request.form.get("response_url")
#
#     somedata = {}
#
#     thr = Thread(target=backgroundworker, args=[somedata,response_url])
#     thr.start()
#
#     return jsonify(message= "working on your request")

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
