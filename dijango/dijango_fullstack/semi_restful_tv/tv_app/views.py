from django.shortcuts import render, redirect
from .models import *

# Create your views here.


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
        'row': Show.objects.get(id=id)
    }
    return render(request, "tv_shows_edit.html", context)


def create_show(request):

    Show.objects.create(
        title=request.POST['title'], network=request.POST['network'], released_date=request.POST['released_date'], description=request.POST['desc'])
    x = Show.objects.last()
    return redirect("/shows/"+str(x.id))


def update_show(request, id):

    c = Show.objects.get(id=id)
    c.title = request.POST['title']
    c.released_date = request.POST['released_date']
    c.network = request.POST['network']
    c.description = request.POST['desc']
    c.save()
    y = id
    return redirect(f"/shows/{y}")


def delete(request, id):
    x = Show.objects.get(id=id)
    x.delete()
    return redirect("/shows")
