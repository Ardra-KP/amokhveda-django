from django.shortcuts import render
from django.http import HttpResponse
from .models import Classes,Experts
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def classes(request):
    classes = Classes.objects.all()  # 👈 Use the correct model name
    return render(request, 'classes.html', {'classes': classes})

def experts(request):
    dict_experts ={
        'experts':Experts.objects.all()
    }
    return render(request,'experts.html',dict_experts)

def events(request):
    return render(request,'events.html')

def contact (request):
    return render(request,'contact.html')
