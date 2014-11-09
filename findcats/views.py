from django.shortcuts import render
from django.http import HttpResponse
import urllib2

# Create your views here.
def index(request):
    req = urllib2.Request('https://api.imgur.com/3/image/igmyoeU')
    req.add_header('Authorization', 'Client-ID 195fbce43dd974e')
    resp = urllib2.urlopen(req)
    content = resp.read()

    context = {'latest_poll_list': content}
    return render(request, 'findcats/index.html', context)
    #return HttpResponse(content)

def results(request, cat_id):
    return HttpResponse("You're looking at the results of poll %s." % cat_id)
