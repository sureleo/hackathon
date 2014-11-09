from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml import Response

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

@csrf_exempt
def sms(request):
#    r = Response()
#    r.message('Hello from your Django app!')
#    return r
    link = "http://623cb0bd.ngrok.com/findcats/"
    name = request.POST.get('Body', '')
    msg = 'Are you looking for a %s? Check %s and Good Luck ^_^.' (name, link)
    twiml = '<Response><Message>' + msg + "</Message></Response>"
    return HttpResponse(twiml, content_type='text/xml')
    #r = Response()
    #r.message('Hello from your Django app!')
    #return r
