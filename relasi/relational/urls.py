from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductList.as_view()),
    path('books/', views.BookList.as_view()),
    path('authors/', views.AuthorList.as_view()),
]
