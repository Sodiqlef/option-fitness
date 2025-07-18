from django.shortcuts import render, HttpResponse
from .models import Trainer, Blog

# Create your views here.

def home(req):
    trainers = Trainer.objects.all()
    blogs = Blog.objects.all()
    return render(req, "home.html", {"trainers": trainers, "blogs":blogs})