from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

value = ""
def getdata(request):
    global value
    if (value == ""):
        return HttpResponse("no data present")
    else:
        return HttpResponse(f'send from esp32 is {value}')

def senddata(request,data):
    global value
    value = data
    return HttpResponse("")

def index(request):
    return HttpResponse('<H1>this is a test server</H1>')