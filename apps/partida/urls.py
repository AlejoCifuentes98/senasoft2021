from django.urls import path
from apps.partida.views import inicio_view, partida_crear_view, partida_ingresar_view, partida_view, preguntar_view, acusar_view, registro_view, login_view, logout_view, perfil_view
urlpatterns = [
    #urls de la aplicación "partida"
    path('', inicio_view, name='inicio'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('perfil/', perfil_view, name='perfil'),
    path('partida/crear', partida_crear_view, name='partida_crear'),
    path('partida/ingresar', partida_ingresar_view, name='partida_ingresar'),
    
    #seccion de partida iniciada
    path('partida/', partida_view, name='partida'),
    path('preguntar/', preguntar_view, name='preguntar'),
    path('acusar/', acusar_view, name='acusar'),
    path('prueba/', turnos_view, name='prueba' )
]