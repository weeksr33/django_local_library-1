from django.urls import path
from . import views

urlpatterns = [

    # catalog/ — The home (index) page.
    path('', views.index, name='index'),

    # catalog/books/ — A list of all books.
    
    # catalog/authors/ — A list of all authors.
    
    # catalog/book/<id> — The detail view for a particular book, with a field primary key of <id> (the default). For example, the URL for the third book added to the list will be /catalog/book/3.
    
    # catalog/author/<id> — The detail view for the specific author with a primary key field of <id>. For example, the URL for the 11th author added to the list will be /catalog/author/11.


]
