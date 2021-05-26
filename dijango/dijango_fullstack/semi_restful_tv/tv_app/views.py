from django.shortcuts import render,redirect,HttpResponse
from . models import *

def root(request):
    return redirect ('/shows')

def index(request):
    context = {
        'shoows': Show.objects.all()
    }
    return render(request, "shows.html", context)


def show_new(request):

    return render(request, "shows_new.html")


def tv_shows(request, id):
    context = {
        'row': Show.objects.get(id=id)
    }
    return render(request, "tv_shows.html", context)


def tv_shows_edit(request, id):
    context = {
        'row2': Show.objects.get(id=id)
    }
    return render(request, "tv_shows_edit.html", context)


def create_show(request):
    Show.objects.create(
        title=request.POST['title'], network=request.POST['network'], released_date=request.POST['released_date'], 
        description=request.POST['desc'])
    return redirect("/shows/<int:id>")


def update_show(request, id):

    c = Show.objects.get(id=id)
    c.title = request.POST['title']
    c.released_date = request.POST['released_date']
    c.network = request.POST['network']
    c.description = request.POST['description']
    c.save()
    return redirect("/shows/<int:id>")

# def destroy(request):
#     c=Show.objects.get(id=)