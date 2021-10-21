from django.shortcuts import render, redirect
from apps.partida.forms import crear_partida_form, ingresar_partida_form, jugador_form, turno_form
from apps.partida.models import Partida, Jugador, Registro, Turno, Tablero
from apps.cartas.models import Cartas

from random import randint # Funcion para generar los hexadecimales

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())

def partida_crear_view(request):
    if request.method == 'POST':
        form_j = jugador_form(request.POST) #formulario para crear jugador
        if form_j.is_valid() :
            jugador = form_j.save() #Se guarda el nombre ingreado en el formulario por parte del jugador    
            r = (randint(0, 10000000000))#Tomar rangos de numeros desde el 0 hasta un valor en especifico
            c= hex(r) [2:] #Se pasa los numeros a hexadecimal, ademas se quita el prefijo "0x" el cual viene con todos los numeros hexadecimales
            codigo = ("{:.5}".format(c)) #formatear el hexadecimal para obtener solo 5 digitos
            
            #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
            modulo = Cartas.objects.filter(tipo__nombre = "mod").order_by('?').first()
            error = Cartas.objects.filter(tipo__nombre = "err").order_by('?').first()
            desarrollador = Cartas.objects.filter(tipo__nombre = "dev").order_by('?').first()

            partida = Partida.objects.create(
                codigo_ingreso=codigo,#se captura l codigo y se pasa como parametro a la tabla Partida  
                carta_err=error.id, 
                carta_mod=modulo.id,
                carta_des=desarrollador.id,)  
            Registro.objects.create(jugador=jugador, partida=partida, jugador_numero='jugador 1')
            
    else:
        form_j = jugador_form() #Si es un metodo Get, se pintará el formulario para ingresar el nombre del jugador
        return render(request, 'partida/partida_crear.html',locals())        
    return render(request, 'partida/partida_crear.html',locals())

def partida_ingresar_view(request):
    if request.method == 'POST':
        form_i=ingresar_partida_form(request.POST)
        if form_i.is_valid():
            nom = form_i.cleaned_data['nombre']
            cod = form_i.cleaned_data['codigo']
            jug = Jugador.object.create(nombre=nom)
            juego = Partida.objects.get(codigo_ingreso=cod)
            Registro.objects.create(jugador= jug.id, partida=juego.id)

    else:
        form_i=ingresar_partida_form()
    return render(request, 'partida/partida_ingresar.html',locals())

def partida_view(request):
    jugador = Jugador.objects.get(jugador=request.user.id)
    registro = Registro.object.get(jugador = jugador)
    return render(request, 'partida/partida.html')

def preguntar_view(request):
    return render(request, 'partida/preguntar.html')

def acusar_view(request):

    return render(request, 'partida/acusar.html')

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