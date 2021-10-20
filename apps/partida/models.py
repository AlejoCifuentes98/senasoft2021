from django.db import models
from django.contrib.auth.models import User

#choices para los jugadores
jugador_num = (
    ('jugador 1','jugador 1'),
    ('jugador 2','jugador 2'),
    ('jugador 3','jugador 3'),
    ('jugador 4','jugador 4'),
)

#Choices para los tipos de turnos
tipo_turno = (
    ('preguntar','preguntar'),
    ('acusar','acusar'),
)

#Modelo para almacenar los jugadores de la partida    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

#Modelo de la partida
class Partida(models.Model):
    codigo_ingreso = models.CharField(max_length=5) #codigo para unirse a la partida
    # carta_des = models.PositiveIntegerField() #Carta a ocultar de los desarrolladores
    # carta_mod = models.PositiveIntegerField() #Carta a ocultar de los modulos
    # carta_err = models.PositiveIntegerField() #Carta a ocultar de los errores

#Modelo para almacenar los datos de la partida  

class Registro(models.Model):
    jugador_numero = models.CharField(max_length=20, choices=jugador_num)
    jugador = models.ForeignKey(Jugador, on_delete=models.PROTECT) #llave foranea de la tabla Jugador
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT) #llave foranea de la tabla Partida
    def __str__(self):
        return self.jugador.nombre + ' ' +self.partida.codigo + ' ' + self.jugador_numero

#Modelo de Turnos
class Turno(models.Model):
    carta_des = models.CharField(max_length=20)
    carta_mod = models.CharField(max_length=20)
    carta_err = models.CharField(max_length=20)
    
    cartas = models.CharField(max_length=20, null=True, blank=True)
    carta_correcta = models.PositiveIntegerField(null=True, blank=True)

    respuesta_jugador_1 = models. PositiveIntegerField(null=True, blank=True)
    respuesta_jugador_2 = models. PositiveIntegerField(null=True, blank=True)
    respuesta_jugador_3 = models. PositiveIntegerField(null=True, blank=True)

    jugador_pregunta = models.PositiveIntegerField() 
    jugador_responde = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20, choices=tipo_turno)

    registro =models.ForeignKey(Registro, on_delete=models.PROTECT)
    def __str__(self):
        return self.registro.jugador.nombre+ ' '+self.carta_des+' '+self.carta_mod+' '+self.carta_err

#Modelo para el Tablero
class Tablero(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.PROTECT)
    
    #cartas tipo desarrollador
    carta_des_1 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_2 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_3 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_4 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_5 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_6 = models.CharField(max_length=50, null=True, blank=True)
    carta_des_7 = models.CharField(max_length=50, null=True, blank=True)
    
    #Cartas tipo modulos
    carta_mod_1 = models.CharField(max_length=50, null=True, blank=True)
    carta_mod_2 = models.CharField(max_length=50, null=True, blank=True)
    carta_mod_3 = models.CharField(max_length=50, null=True, blank=True)
    carta_mod_4 = models.CharField(max_length=50, null=True, blank=True)
    carta_mod_5 = models.CharField(max_length=50, null=True, blank=True)
    carta_mod_6 = models.CharField(max_length=50, null=True, blank=True)
    
    #cartas tipo errores
    carta_err_1 = models.CharField(max_length=50, null=True, blank=True)
    carta_err_2 = models.CharField(max_length=50, null=True, blank=True)
    carta_err_3 = models.CharField(max_length=50, null=True, blank=True)
    carta_err_4 = models.CharField(max_length=50, null=True, blank=True)
    carta_err_5 = models.CharField(max_length=50, null=True, blank=True)
    carta_err_6 = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.registro.jugador.nombre

      