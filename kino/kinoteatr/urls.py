from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('session/<int:pk>/', views.session_detail, name='session_detail'),
    path('book/<int:session_id>/', views.book_ticket, name='book_ticket'),


]