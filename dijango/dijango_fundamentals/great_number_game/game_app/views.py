import random
from django.shortcuts import render, redirect


def index(request):
    request.session['number']=random.randint(1, 100)
    print(request.session['number'])
    return render(request,"index.html")


def process(request):
    if request.method == 'POST':
        number = request.session['number']
        guess = int(request.POST['number_from_user'])

        if number == guess:
            request.session['color'] = 'green'
            print('green')
            request.session['string'] = f"{number} was the number"

        elif number > guess:
            request.session['color'] = 'red'
            request.session['string'] = 'Too low'
            print('red')
            
        else:
            request.session['color'] = 'red'
            print('white')
            request.session['string'] = 'Too high'

    return redirect('/')
    
