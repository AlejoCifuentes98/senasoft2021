from django.shortcuts import redirect, render
from .models import Cartas
from apps.partida.models import Partida


def cartas_ocultas(request,id_partida):
    partida = Partida.objects.get(id = id_partida)
    #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
    modulo = Cartas.objects.filter(tipo__nombre = "mod").order_by('?').first()
    error = Cartas.objects.filter(tipo__nombre = "err").order_by('?').first()
    desarrollador = Cartas.objects.filter(tipo__nombre = "dev").order_by('?').first()
    #Guarda en la partida las cartas secretas
    partida.carta_des = desarrollador.id
    partida.carta_mod = modulo.id
    partida.carta_err = error.id
    partida.save()
    #Excluye las cartas que van a hacer las ocultas y mezcla las cartas
    cartas_random = Cartas.objects.exclude(id = modulo.id).exclude( id = error.id).exclude(id = desarrollador.id).order_by('?')
    lts = []
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    
    for i in cartas_random:
        #Llena la lista lts
        lts.append(i)
    #Divide la lista en 2
    lts_1 = lts[:len(lts)//2]
    lts_2 = lts[len(lts)//2:]
    #Divide la lista en 4
    jugador1 = lts_1[:len(lts_1)//2]
    jugador2 = lts_1[len(lts_1)//2:]
    jugador3 = lts_2[:len(lts_2)//2]
    jugador4 = lts_2[len(lts_2)//2:]
    
    print(jugador1)
    print(jugador2)
    print(jugador3)
    print(jugador4)

    opciones=[]
    lista =["22222", "queso", "help me", "banana", "1","3","4"]

    x = ["apple", "banana", "4"] 
    for i in lista:
	    if i in x:
		    opciones.append(i)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(opciones)
			

    return redirect('/')


def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "mod")
    lista_error = Cartas.objects.filter(tipo__nombre = "err")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "dev")
    return render(request, 'cartas/lista_cartas.html',locals())

def cartas_juego():
    pass

