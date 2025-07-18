from django.shortcuts import render, HttpResponse
from .models import Trainer

# Create your views here.

def home(req):
    trainers = Trainer.objects.all()
    return render(req, "home.html", {"trainers": trainers})