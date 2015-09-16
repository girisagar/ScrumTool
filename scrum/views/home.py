from django.shortcuts import render

def home(request):
    return render(request, "scrum/home.html", {})