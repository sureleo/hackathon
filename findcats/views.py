from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import urllib2
import json
import random

# Create your views here.
def index(request):
    #popular name for cats!
    names = [
        'Bella', 'Tigger', 'Chloe', 'Oliver', 'Shadow',
        'Molly', 'Smokey', 'Kitty', 'Angel', 'Jasper',
        'Lily', 'Tiger', 'Charlie', 'Gizmo', 'Lucy',
        'Oreo', 'Luna', 'Peanut', 'Simba', 'Toby'
    ]
    gender = ['boy', 'girl']
    castrated = ['castrated', 'not castrated']

    req = urllib2.Request('https://api.imgur.com/3/gallery/t/cat/top')
    req.add_header('Authorization', 'Client-ID 195fbce43dd974e')
    resp = urllib2.urlopen(req)
    content = resp.read()
    items = json.loads(content)['data']['items']
    links = []
    for i in items:
        links.append(i['link'])

    context = {
        'name': random.choice(names),
        'gender': random.choice(gender),
        'castrated': random.choice(castrated),
        'pic': random.choice(links)
    }
    return render(request, 'findcats/index.html', context)

def results(request, cat_id):
    return HttpResponse("You're looking at the results of poll %s." % cat_id)
