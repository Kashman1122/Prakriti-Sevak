from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def landing(request):
    return render(request,'landing.html')