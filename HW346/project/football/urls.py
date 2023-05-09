from django.urls import path
from . import views

urlpatterns = [
    path('players', views.player, name='profile'),
    path('clubs', views.club, name='clubs'),
    path('matches', views.match, name='matches'),
]
