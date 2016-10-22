from django.shortcuts import render
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request,'home.html', {})

def login(request):
    return render(request, "login.html", {})

def logout(request):
    return render(request, "logout.html", {'username': auth.get_user(request).username})