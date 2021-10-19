from django.shortcuts import render
from apps.partida.forms import crear_partida_form, ingresar_partida_form

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())

def partida_crear_view(request):
    if request.method == 'POST':
        formulario = crear_partida_form(request.POST)
        if formulario.is_valid():
            formulario.save
            print("Partida creada con exito")
    else: 
        formulario = ingresar_partida_form()
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
