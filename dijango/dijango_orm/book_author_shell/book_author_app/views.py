from django.http import request
from book_author_app import models
from django.shortcuts import redirect, render
from . import models

def index(request):
    context={
        'books': models.allBook()
    }

    return render(request, 'index.html',context)

def addBook (request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        newly_created_book=models.addOneBook(title,desc)
        return redirect('/')

def showBook(request,id):
    context={
        'this_book':models.getBook(id),
        'all_author':models.allAuthor()
    }
    return render(request,"book.html",context)

def addAuthorToBook(request,book_id):
    if request.method=='POST':
        id=request.POST['select_author']
        print(id)
        models.add_auothor_to_book(id,book_id=book_id)
        return redirect(f'/book/{book_id}')

def authors(request):
    context={
        'authors': models.allAuthor()

    }

    return render(request,'author.html',context)

def showAuthor(request,id):
    context ={
        'this_author':models.getauthor(id),
        'all_books': models.allBook()
    }
    return render(request,'authorShow.html',context)

def addAuthor(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name=request.POST['last_name']
        note=request.POST['note']

        models.addOneAuthor(first_name,last_name,note)
        return redirect('/authors')

def addBookToAuthor(request,auth_id):
    if request.method=='POST':
        id=request.POST['select_book']
        models.add_book_to_author(id,auth_id)
        return redirect(f'/authors/{auth_id}')



