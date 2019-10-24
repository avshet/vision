from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from hello.vision_api import vision_face_detection

# Create your views here.
def index(request):
     return HttpResponse(vision_face_detection())
#    
#    return render(request, "index.html")


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
