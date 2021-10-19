from django.shortcuts import render

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())

def partida_crear_view(request):
    
    return render(request, 'partida/partida_crear.html',locals())

def partida_ingresar_view(request):
    return render(request, 'partida/partida_ingresar.html',locals())

