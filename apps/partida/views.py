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
    else: 
        formulario = ingresar_partida_form()
        return render(request, 'partida/partida_crear.html',locals())        
    return render(request, 'partida/partida_crear.html',locals())

def partida_ingresar_view(request):

    return render(request, 'partida/partida_ingresar.html',locals())

