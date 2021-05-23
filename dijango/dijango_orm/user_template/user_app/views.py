from django.shortcuts import redirect, render,HttpResponse
from .models import User

def index(request):
    context={
        'users': User.objects.all()
    }
    return render(request, 'index.html',context)

def add(request):
    
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], age=request.POST['age'] )
    return redirect('/')

