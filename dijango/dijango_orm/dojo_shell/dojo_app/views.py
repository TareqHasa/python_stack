from django.shortcuts import render, redirect
from . models import *

def index(request):
    data= Dojo.objects.all()
    context={
        'dojos':data,
        'ninjas':Ninja.objects.all()
    }
    return render(request,"index.html",context)

def add_dojo(request):
    if request.POST['name'] not in Dojo.name:
        Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],
        state=request.POST['state'],desc="new dojo")
    
    return redirect('/')

def add_ninja(request):
    
    Ninja.objects.create(first_name=request.POST['first'],last_name=request.POST['last'], dojo=Dojo.objects.get(name=request.POST['dojo_']))

    return redirect('/')