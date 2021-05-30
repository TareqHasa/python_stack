from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from . models import *
import re
import bcrypt

def root(request):
    return render (request,'index.html')

def regester(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors={}
    if len( request.POST['first_name'])<2:
        errors['first_name']="first name is too short"
    if len( request.POST['first_name'])<2:
        errors['last_name']="last name is too short"

    if not EMAIL_REGEX.match(request.POST['email']):            
        errors['email'] = "Invalid email address!"

    if len(request.POST['password'])<8:
        errors['password']="short password"

    if request.POST['password'] != request.POST['c_password']:
        errors['password']="Not matching"

    if len (errors)>0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect('/')
    else:
        first_name=request.POST['first_name']        
        last_name=request.POST['first_name']        
        email=request.POST['email']        
        password=request.POST['password']  
        c_password=request.POST['c_password']
        if password==c_password:
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=first_name,last_name=last_name,email=email,pasword=hash1)
            if 'name' not in request.session:
                request.session['name']=first_name
                return redirect('/success')
        return redirect('/')
            

def success(request):
    if 'name' in request.session:
        return render(request,'success.html')
    return redirect('/')

def logout(request):
    del request.session['name']
    return redirect('/')

def login(request):
    lerrors={}
    user = User.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.pasword.encode()):
            request.session['name'] = logged_user.first_name
            return redirect('/success')
    lerrors['lpassword']="wrong password"
    if len (lerrors)>0:
        for key, value in lerrors.items():
                messages.error(request, value)
        return redirect('/')
    return redirect("/")

