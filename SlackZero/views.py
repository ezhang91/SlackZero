from django.http import HttpResponse
from django.shortcuts import render

import json

def verify_email(request):
	return HttpResponse(json.dumps({
		'text': 'ethan is a big butt',
	}))
