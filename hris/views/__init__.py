from django.shortcuts import render
from hris.views.employee import *

def home(request):
    return render(request, "home.html", {})
    
def login(request):
    return render(request, "login.html", {})