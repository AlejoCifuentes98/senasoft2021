from django.shortcuts import redirect, render
from .models import Cartas
from apps.partida.models import Turno
from .forms import turno_form
from apps.partida.models import Partida, Registro, Tablero
from django.db.models import Q

def play_view(request,id_partida):
    partida = Partida.objects.get(id = id_partida)

    #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
    modulo = Cartas.objects.filter(tipo__nombre = "modulo").order_by('?').first()
    error = Cartas.objects.filter(tipo__nombre = "error").order_by('?').first()
    desarrollador = Cartas.objects.filter(tipo__nombre = "desarrollador").order_by('?').first()

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
        lts.append(i.id)

    #Divide la lista en 2
    lts_1 = lts[:len(lts)//2]
    lts_2 = lts[len(lts)//2:]

    #Divide la lista en 4
    jugador1 = lts_1[:len(lts_1)//2]
    jugador2 = lts_1[len(lts_1)//2:]
    jugador3 = lts_2[:len(lts_2)//2]
    jugador4 = lts_2[len(lts_2)//2:]
    print ("xxxxxxxxxxxxx")
    print (jugador1, jugador2, jugador3, jugador4)
    print ("xxxxxxxxxxxxx")
    #Obtiene al jugador 1 le pasa sus cartas y le crea su tablero
    r = Registro.objects.get(partida=partida.id, jugador_numero='jugador 1')
    r.cartas = jugador1
    r.save()
    tablero=Tablero()
    tablero.registro = r
    tablero.save()

    #Obtiene al jugador 2 le pasa sus cartas y le crea su tablero
    r = Registro.objects.get(partida=partida.id, jugador_numero='jugador 2')
    r.cartas = jugador2
    r.save()
    tablero=Tablero()
    tablero.registro=r
    tablero.save()

    #Obtiene al jugador 3 le pasa sus cartas y le crea su tablero
    r = Registro.objects.get(partida=partida.id, jugador_numero='jugador 3')
    r.cartas = jugador3
    r.save()
    tablero=Tablero()
    tablero.registro=r
    tablero.save()

    #Obtiene al jugador 4 le pasa sus cartas y le crea su tablero
    r = Registro.objects.get(partida=partida.id, jugador_numero='jugador 4')
    r.cartas = jugador4
    r.save()
    tablero=Tablero()
    tablero.registro=r
    tablero.save()

    return redirect('/jugar/{}/'.format(partida.id))


def juego_view(request, id_partida):
    partida=Partida.objects.get(id = id_partida)
    registro = Registro.objects.get(jugador= request.user.id)
    lista_modulo = Cartas.objects.filter(tipo__nombre = "modulo")
    lista_error = Cartas.objects.filter(tipo__nombre = "error")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "desarrollador")

    lista = registro.cartas # '[1,4,5,6]'

    # Convirtiendo la cadena a lista
    print ("cadena inicial", lista)
    res = lista.strip('][').split(', ')
    # consultando las tarjetas asignadas por el sistema
    cartas = Cartas.objects.filter(Q(id = res[0])|Q(id = res[1])|Q(id = res[2])|Q(id = res[3]))
    print(cartas)
    if request.method =='POST':
        form_t=turno_form(request.POST)
        if form_t.is_valid():
            des = form_t.cleaned_data['desa']
            err = form_t.cleaned_data['erro']
            mod = form_t.cleaned_data['modu']
            Turno.objects.create(
                carta_des=des.id, 
                carta_err=err.id, 
                carta_mod=mod.id,
                jugador_pregunta= request.userid,
                )
    else:
        form_t=turno_form()
    return render(request, 'cartas/juego.html', locals())


def lista_(request):
    lista_modulo = Cartas.objects.filter(tipo__nombre = "mod")
    lista_error = Cartas.objects.filter(tipo__nombre = "err")
    lista_desarrollador = Cartas.objects.filter(tipo__nombre = "dev")
        
    
    return render(request, 'cartas/lista_cartas.html',locals())

def turnos_view(request):
    #jugador= Jugador.objects.get(jugador=id_jugador)
    if request.method =='POST':
        form_t=turno_form(request.POST)
        if form_t.is_valid():
            des = form_t.cleaned_data['desa']
            err = form_t.cleaned_data['erro']
            mod = form_t.cleaned_data['modu']
            # Turno.objects.create(
            #     carta_des=des.id, 
            #     carta_err=err.id, 
            #     carta_mod=mod.id,
            #     #jugador_pregunta= jugador.id,
            #     )
    else:
        form_t=turno_form()
    return render(request, 'partida/prueba.html', locals())

def cartas_juego():
    pass

