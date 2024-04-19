from django.shortcuts import render,redirect

def home(request):
    return render(request,'home.html')

def hipage(request):
    return render(request,'hi.html')

def contactme(request):
    return render(request,'contactme.html')