from django.shortcuts import render
from appt.models import Place,Team

def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})

def service(request):
    return render(request,'service.html')