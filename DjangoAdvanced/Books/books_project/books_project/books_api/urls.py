from books_project.books_api import views
from django.urls import path

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='books-list'),
    path('books/<int:id>', views.DetailBookView.as_view(), name='books-details')
] 