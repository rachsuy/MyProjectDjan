from django.http import *
from django.shortcuts import render, HttpResponse

# Create your views here.
def appointment(request):
    test = 'Esdras'
    return render(request, "appointment.html", {'nom': test})

 # Create your views here.
def index(request):
    test = 'Esdras'
    return render(request, "index.html", {'nom': test})

def log(request):
    test = 'Esdras'
    return render(request, "log.html", {'nom':test})
    
    