from django.urls import path
from .views import *
urlpatterns = [
    path('cartas_ocultas/', cartas_ocultas, name = 'cartas_ocultas'),
    path('lista/',lista_, name='lista'),
]
