from django.shortcuts import render,redirect

from projectpg.models import projects

def home(request):
    context=projects.objects.all()
    context={'projects':context}
    return render(request,'home.html',context)
