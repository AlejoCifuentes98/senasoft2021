from django.urls import path
from apps.partida.views import inicio_view, partida_crear_view, partida_ingresar_view, partida_view, preguntar_view, acusar_view
urlpatterns = [
    #urls de la aplicación "partida"
    path('', inicio_view, name='inicio'),
    path('partida/crear', partida_crear_view, name='partida_crear'),
    path('partida/ingresar', partida_ingresar_view, name='partida_ingresar'),
    
    #seccion de partida iniciada
    path('partida', partida_view, name='partida'),
    path('preguntar', preguntar_view, name='preguntar'),
    path('acusar', acusar_view, name='acusar'),
]