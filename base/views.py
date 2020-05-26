from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required





# Create your views here.

def home(request):
    
    return render(request,'index.html',locals())

@login_required(login_url='/accounts/login/')
def about(request):
    
    return render(request,'about.html',locals())



