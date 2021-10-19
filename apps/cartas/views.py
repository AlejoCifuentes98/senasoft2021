from django.shortcuts import render
from .models import Cartas
def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "Modulo")
    lista_error = Cartas.objects.filter(tipo__nombre = "Error")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "Desarrollador")
