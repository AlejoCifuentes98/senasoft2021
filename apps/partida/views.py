from django.shortcuts import render
from apps.partida.forms import crear_partida_form, ingresar_partida_form, jugador_form
from apps.partida.models import Anotacion, Partida
from random import randint

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())

def partida_crear_view(request):
    if request.method == 'POST':
        form_j = jugador_form(request.POST) #formulario para crear jugador
        if form_j.is_valid() :
            form_j.save() #Se guarda el nombre ingreado en el formulario por parte del jugador    
            r = (randint(0, 10000000000))#Tomar rangos de numeros desde el 0 hasta un valor en especifico
            c= hex(r) [2:] #Se pasa los numeros a hexadecimal, ademas se quita el prefijo "0x" el cual viene con todos los numeros hexadecimales
            codigo = ("{:.5}".format(c)) #formatear el hexadecimal para obtener solo 5 digitos
            Partida.objects.create(codigo_ingreso=codigo) #se captura l codigo y se pasa como parametro a la tabla Partida

            return redirect('/partida/')               
    else: 
        form_j = jugador_form() #Si es un metodo Get, se pintará el formulario para ingresar el nombre del jugador
        
        
        return render(request, 'partida/partida_crear.html',locals())        
    return render(request, 'partida/partida_crear.html',locals())

def partida_ingresar_view(request):

    return render(request, 'partida/partida_ingresar.html',locals())

def partida_view(request):
    return render(request, 'partida/partida.html')

def preguntar_view(request):
    return render(request, 'partida/preguntar.html')

def acusar_view(request):
    return render(request, 'partida/acusar.html')
