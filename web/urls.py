from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('plays/', views.plays, name='plays'),
    path('players/', views.players, name='players'),
    path('create/', views.createPlayer, name='createPlayer'),
]