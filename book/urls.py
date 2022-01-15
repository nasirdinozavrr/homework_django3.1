from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_all, name='books'),
    path('books/<int:id>/', views.book_detail, name='book_all'),
    path('add-books/', views.add_book, name='add-books'),
]