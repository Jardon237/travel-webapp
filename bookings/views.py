from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def seat(request):
    return render (request, 'seat.html')

def signin(request):
    return render (request, 'signin.html')   

def signup(request):
    return render (request, 'signup.html')

def available(request, *args, **kwargs):
    return render(request, 'available.html')

