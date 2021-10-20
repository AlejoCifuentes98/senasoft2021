from django.shortcuts import redirect, render
from .models import Cartas, Cartas_Ocultas


def cartas_ocultas(request):
    #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
    modulo = Cartas.objects.filter(tipo__nombre = "mod").order_by('?').first()
    error = Cartas.objects.filter(tipo__nombre = "err").order_by('?').first()
    desarrollador = Cartas.objects.filter(tipo__nombre = "dev").order_by('?').first()
    #Excluye las cartas que van a hacer las ocultas
    cartas_random = Cartas.objects.exclude(id = modulo.id).exclude( id = error.id).exclude(id = desarrollador.id).order_by('?')
    lts = []
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    
    for i in cartas_random:
        lts.append(i)
    lts_1 = lts[:len(lts)//2]
    lts_2 = lts[len(lts)//2:]
    jugador1 = lts_1[:len(lts_1)//2]
    jugador2 = lts_1[len(lts_1)//2:]
    jugador3 = lts_2[:len(lts_2)//2]
    jugador4 = lts_2[len(lts_2)//2:]
    
    print(jugador1)
    print(jugador2)
    print(jugador3)
    print(jugador4)

    return redirect('/')


def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "mod")
    lista_error = Cartas.objects.filter(tipo__nombre = "err")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "dev")
    return render(request, 'cartas/lista_cartas.html',locals())

def cartas_juego():
    pass

