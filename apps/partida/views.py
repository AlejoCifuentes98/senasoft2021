from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from apps.partida.forms import crear_partida_form, ingresar_partida_form, jugador_form, registro_form, login_form
from apps.partida.models import Partida, Jugador, Registro, Turno, Tablero
from apps.cartas.models import Cartas

from random import randint # Funcion para generar los hexadecimales

#Vistas de la aplicación "partida"
def inicio_view(request):
    return render(request, 'partida/inicio.html',locals())


def partida_crear_view(request):
    jugador = Jugador.objects.get(id=request.user.id)
    if request.method == 'POST': 
        form_p = crear_partida_form(request.POST)       
        if form_p.is_valid():
            
            r = (randint(0, 10000000000))#Tomar rangos de numeros desde el 0 hasta un valor en especifico
            c= hex(r) [2:] #Se pasa los numeros a hexadecimal, ademas se quita el prefijo "0x" el cual viene con todos los numeros hexadecimales
            codigo = ("{:.5}".format(c)) #formatear el hexadecimal para obtener solo 5 digitos
            
            #Obtiene el primer objecto que se obtiene de un orden random de cada tipo
            # modulo = Cartas.objects.filter(tipo__nombre = "mod").order_by('?').first()
            # error = Cartas.objects.filter(tipo__nombre = "err").order_by('?').first()
            # desarrollador = Cartas.objects.filter(tipo__nombre = "dev").order_by('?').first()

            partida = Partida()
            partida.codigo_ingreso=codigo#se captura el codigo y se pasa como parametro a la tabla Partida  
            partida.save()
                # carta_err=error.id, 
                # carta_mod=modulo.id,
                # carta_des=desarrollador.id,)  
            registro = Registro()
            registro.jugador = jugador
            registro.partida = partida
            registro.jugador_numero = 'jugador 1'
            registro.save 
            return redirect('/partida/')
    else:
        form_u = registro_form() #Si es un metodo Get, se pintará el formulario para ingresar el nombre del jugador
        form_j = jugador_form()
        return render(request, 'partida/partida_crear.html',locals())        
    return render(request, 'partida/partida_crear.html',locals())

def registro_view(request):
    #seccion para crear una cuenta
    if request.method == 'POST':
        form_r =  registro_form(request.POST) #formulario para crear registrar 
        form_j = jugador_form(request.POST)
        
        #usuario en la tabla User de django y la tabla jugador
        if form_r.is_valid() and form_j.is_valid(): #validar si el formulario es valido
            username =  form_r.cleaned_data['username'] #username 
            clave_1 = form_r.cleaned_data['clave_1'] #Ingresar clave 1
            clave_2 = form_r.cleaned_data['clave_2'] #Ingresar clave 2
            u = User.objects.create_user(username= username, password= clave_2, is_superuser=False, is_staff=True) #Se crea el usuario
            j = Jugador()
            j.usuario = u
            j.save()
            return redirect('/login/')
    else: 
        form_r = registro_form() 
        form_j = jugador_form()     
        return render(request, 'partida/registro.html', locals())   
    return render(request, 'partida/registro.html', locals())

def login_view(request):
    #seccion para loguearse 
    usu = "" #variable para almacenar el username
    cla = "" #variable para almacenar la clave
    if request.method == 'POST':
        form_l = login_form(request.POST)
        if form_l.is_valid():
            #Validaciones para el usuario y la contraseña
            usu = form_l.cleaned_data['username'] 
            cla = form_l.cleaned_data['clave']
            usuario =authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/perfil/')
            else:
                msj = 'Sus credenciales son incorrectas, verifique e intente nuevamente.'
    else: 
        form_l = login_form()                 
        return render(request, 'partida/login.html', locals())
    return render(request, 'partida/login.html', locals())

def logout_view(request):
    logout(request)
    return redirect ('/login/')

def perfil_view(request):
    jugador = User.objects.get(id=request.user.id)
    partidas = Registro.objects.filter() 
    return render(request, 'partida/perfil.html',locals())
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
    # registro = Registro.object.get(jugador = jugador)
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