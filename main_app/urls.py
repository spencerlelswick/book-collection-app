from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('books/', views.books_index, name='index'),
  path('books/<int:book_id>/', views.books_detail, name='detail'),
]
