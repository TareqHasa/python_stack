from django.shortcuts import redirect, render, HttpResponse
import random
from time import strftime

def root(request):
    if 'gold' not in request.session :
        request.session['gold']=0
        request.session['activities']=[]

    context={
        'gold':request.session['gold'],
        'activities':request.session['activities'],

    }

    return render (request,'index.html',context)

def process(request):
    if request.POST['gold']=='farm':
        x=random.randint(10,20)
        request.session['gold']+=x
        request.session['activities'].append(f"Earned {str(x)} golds from farm! {strftime('%Y-%m-%d %H:%M %p')}")

    elif request.POST['gold']=='cave':
        x=random.randint(5,10)
        request.session['gold']+=x
        request.session['activities'].append(f"Earned {str(x)} golds from cave! {strftime('%Y-%m-%d %H:%M %p')}")
    elif request.POST['gold']=='house':
        x=random.randint(2,5)
        request.session['gold']+=x
        request.session['activities'].append(f"Earned {str(x)} golds from house! {strftime('%Y-%m-%d %H:%M %p')}")
    elif request.POST['gold']=='casino':
        x=random.randint(-50,50)
        if x >= 0:
            request.session['gold']+=x
            request.session['activities'].append(f"Earned {str(x)} golds from casino! {strftime('%Y-%m-%d %H:%M %p')}")
        else:
            request.session['gold']+=x
            request.session['activities'].append(f"Enterd a Casino and lost {str(x*-1)} golds ...ouch... {strftime('%Y-%m-%d %H:%M %p')}")

    return redirect('/')


def reset(request):
    if request.POST['reset']=='reset':
        if 'gold' in request.session:
            del request.session['gold']
            del request.session['activities']
        return redirect('/')
