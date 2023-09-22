from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('books/', views.books_index, name='index'),
  path('books/<int:book_id>/', views.books_detail, name='detail'),
  path('books/create/', views.BookCreate.as_view(), name='books_create'),
  path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
  path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
]
