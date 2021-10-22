from django.urls import path
from .views import *
urlpatterns = [
    
    path('lista/',lista_, name='lista'),
    path('partida/play/<int:id_partida>/', play_view, name='partida_play'),
    path('jugar/<int:id_partida>/', juego_view, name='jugar'),
]
