from book_author_app.views import authors
from django.db import models
from django.db.models.fields import CharField

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField(default="no description")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    note=models.TextField(default="no comments")
    book=models.ManyToManyField(Book,related_name='authors')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def addOneBook(title,desc):
    return Book.objects.create(title=title,desc=desc)

def allBook():
    return Book.objects.all()

def getBook(id):
    return Book.objects.get(id=id)

def allAuthor():
    return Author.objects.all()

def add_auothor_to_book(id,book_id):
    author=Author.objects.get(id=id)
    book=Book.objects.get(id=book_id)
    added_author= book.authors.add(author)
    return added_author

def getauthor(id):
    return Author.objects.get(id=id)

def addOneAuthor(first_name,last_name,note):
    new_author = Author.objects.create(first_name=first_name,last_name=last_name,note=note)
    return new_author

def add_book_to_author(id,auth_id):
    author=Author.objects.get(id=auth_id)
    book=Book.objects.get(id=id)
    added_book=author.book.add(book)
    return added_book
