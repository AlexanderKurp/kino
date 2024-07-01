from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, LogoutUser

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/sessions/', views.movie_sessions, name='movie_sessions'),
    path('session/<int:pk>/', views.session_detail, name='session_detail'),
    path('book/<int:session_id>/', views.book_ticket, name='book_ticket'),
    path('actor/', views.actor_list, name='actor_list'),
    path('actor/<int:pk>/', views.actor_detail, name='actor_detail'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:pk>/', views.director_detail, name='director_detail'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('movies/', views.movie_list, name='movie_list'),

]
