from django.urls import path
from apps.partida.views import inicio_view, partida_crear_view, partida_ingresar_view
urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('partida/crear', partida_crear_view, name='partida_crear'),
    path('partida/ingresar', partida_ingresar_view, name='partida_ingresar'),
]