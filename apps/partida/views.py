from django.shortcuts import render
from apps.partida.forms import crear_partida_form, ingresar_partida_form, jugador_form
from random import randint

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())

def partida_crear_view(request):
    if request.method == 'POST':
        form_j = jugador_form(request.POST)
        form_p = crear_partida_form(request.POST)
        if form_j.is_valid() and form_p.is_valid():
            
            p = form_p.save(commit=False)
            form_j.save() 
            
                
            r = (randint(0, 10000000000))
            c= hex(r) [2:]
            codigo = ("{:.5}".format(c))
            p.codigo_ingreso = codigo
            p.save()    
            print("Partida creada con exito")
             
             
    else: 
        form_j = jugador_form(request.POST)
        form_p = crear_partida_form(request.POST)
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
