from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "myapp"

urlpatterns = [
    # Index Page
    path('', views.home, name="home"),

    # Home Page
    path('about', views.about, name="about"),

    # Advertise Page
    path('advertise', views.advertise, name="advertise"),

    # Equipment Page
    path('equipment', views.equipment, name="equipment"),

    # SignIn Page
    path('signin', views.signin, name="signin"),

    # Contact Page
    path('contact', views.contact, name="contact"),
]
