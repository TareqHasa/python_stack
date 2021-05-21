from django.shortcuts import render, redirect,HttpResponse
import random

y=random.randint(1, 100)

def index(request):
    if 'number' in request.session:
        request.session['number']=request.POST['number_from_user']
        context={
            'num' : y
        }
        return render(request,"index.html",context)

    else:
        request.session['number']=0
        return render(request,'index.html')