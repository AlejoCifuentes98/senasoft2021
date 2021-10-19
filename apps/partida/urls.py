from django.urls import path
urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('partida/crear', crear_partida_view, name='crear_partida'),
    path('partida/ingresar', partida_ingresar_view, name='partida_ingresar'),
]