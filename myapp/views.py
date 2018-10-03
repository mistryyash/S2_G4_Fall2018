from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def advertise(request):
    return render(request, "advertise.html")

def signin(request):
    return render(request, "signin.html")

def contact(request):
    return render(request, "contact.html")

def equipment(request):
    return render(request, "sportequip.html")