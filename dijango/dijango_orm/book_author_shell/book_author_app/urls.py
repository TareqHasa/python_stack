from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook',views.addBook),
    path('book/<int:id>',views.showBook),
    # path('/addbook/<int:id>/<int:book_id>',views.addAuthorToBook)
    path ('book/addAouthorToBook/<int:book_id>',views.addAuthorToBook),
    path('authors',views.authors),
    path('authors/<int:id>',views.showAuthor),
    path('addAuthor',views.addAuthor),
    path('authors/addOneBookToAuthor/<int:auth_id>',views.addBookToAuthor)
]
