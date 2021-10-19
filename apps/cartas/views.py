from django.shortcuts import render
from .models import Cartas, Cartas_Ocultas
import random

def cartas_ocultas():
    #Cuenta el numero de cartas existentes por cada tipo
    numero_modulo = Cartas.objects.filter(tipo__nombre = "Modulo").count()
    numero_error = Cartas.objects.filter(tipo__nombre = "Error").count()
    numero_desarrollador = Cartas.objects.filter(tipo__nombre = "Desarrollador").count()
    #Guarda un número random entre el 1 y el numero total de cartas en cada tipo
    n_modulo = random.randint(1,numero_modulo)
    n_error = random.randint(1,numero_error)
    n_desarrollador = random.randint(1,numero_desarrollador)
    #Busca el la base de datos el número ramdon igualandolo al id
    modulo = Cartas.objects.filter(id = n_modulo)
    error = Cartas.objects.filter(id = n_error)
    desarrollador = Cartas.objects.filter(id = n_desarrollador)
    #Crea objecto con las caras ocultas
    Cartas_Ocultas.objects.Create(carta_des=desarrollador.id, carta_mod=modulo.id, carta_err=error.id)

def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "Modulo")
    lista_error = Cartas.objects.filter(tipo__nombre = "Error")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "Desarrollador")
