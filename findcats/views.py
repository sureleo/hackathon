from django.shortcuts import render
from django.http import HttpResponse
import urllib2

# Create your views here.
def index(req):
    req = urllib2.Request('https://api.imgur.com/3/gallery/t/cat/top')
    req.add_header('Authorization', 'Client-ID 195fbce43dd974e')
    resp = urllib2.urlopen(req)
    content = resp.read()
    return HttpResponse(content)
