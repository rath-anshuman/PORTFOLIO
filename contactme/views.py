from django.shortcuts import render


from contactme.models import sayhi
from contactme.models import contact
# Create your views here.


def hipage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('textarea')
        hi=sayhi.objects.create(name=name,email=email, message=message)
        hi.save()
        return render(request,'thankyou.html')
    return render(request,'hi.html')

def contactme(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        project_type = request.POST.get('project_type')
        message = request.POST.get('message')
        cntct=contact.objects.create(name=name, email=email, project_type=project_type, message=message)
        cntct.save()
        return render(request,'thankyou.html')
    return render(request,'contactme.html')