from django.shortcuts import render
from ffapi.models import Character

# Create your views here.


def home(req):
    

    return render(req, "ffweb/home.html", {
        'page': 'home'
    })





def about(req):
    

    return render(req, "ffweb/about.html", {
        'page': 'about'
    })


def documentation(req):

    return render(req, 'ffweb/documentation.html', {
        "page": 'documentation'
    })