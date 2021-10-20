from django.shortcuts import redirect, render
from .models import Cartas, Cartas_Ocultas
from django.db.models import Q
import random

def cartas_ocultas(request):
    #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
    modulo = Cartas.objects.filter(tipo__nombre = "mod").order_by('?').first()
    error = Cartas.objects.filter(tipo__nombre = "err").order_by('?').first()
    desarrollador = Cartas.objects.filter(tipo__nombre = "dev").order_by('?').first()
    #Excluye las cartas que van a hacer las ocultas
    cartas_random = Cartas.objects.exclude(id = modulo.id).exclude( id = error.id).exclude(id = desarrollador.id) 
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    i = -1
    for i in cartas_random:
        jugador1.append(cartas_random[i+1])
        if i>3:
            jugador2.append(cartas_random[i+1])
            if i>7:
                jugador3.append(cartas_random[i+1])
                if i>11:
                    jugador4.append(cartas_random[i+1])

    print(jugador1)

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    #print (lst)
    return redirect('/')


def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "mod")
    lista_error = Cartas.objects.filter(tipo__nombre = "err")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "dev")
    return render(request, 'cartas/lista_cartas.html',locals())

def cartas_juego():
    pass

