from django.db import models
jugador_num = (
    ('jugador 1','jugador 1'),
    ('jugador 2','jugador 2'),
    ('jugador 3','jugador 3'),
    ('jugador 4','jugador 4'),
)
tipo_turno = (
    ('preguntar','preguntar'),
    ('acusar','acusar'),
)

#Modelo para almacenar los jugadores de la partida    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Partida(models.Model):
    codigo_ingreso = models.CharField(max_length=5)
    carta_des = models.PositiveSmallIntegerField()
    carta_mod = models.PositiveSmallIntegerField()
    carta_err = models.PositiveSmallIntegerField()

class Registro(models.Model):
    jugador_numero = models.CharField(max_length=20, choices=jugador_num)
    jugador = models.ForeignKey(Jugador, on_delete=models.PROTECT)
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT)
    def __str__(self):
        return self.jugador.nombre + ' ' +self.partida.codigo + ' ' + self.jugador_numero

class Turno(models.Model):
    carta_des = models.Charfield(max_length=20)
    carta_mod = models.Charfield(max_length=20)
    carta_err = models.Charfield(max_length=20)
    
    cartas = models.Charfield(max_length=20, null=True, blank=True)
    carta_correcta = models.PositiveIntegerField(null=True, blank=True)

    respuesta_jugador_1 = models. PositiveIntegerField(null=True, blank=True)
    respuesta_jugador_2 = models. PositiveIntegerField(null=True, blank=True)
    respuesta_jugador_3 = models. PositiveIntegerField(null=True, blank=True)
    
    registro =models.ForeignKey(Registro, on_delete=models.PROTECT)
     
#Modelo para almacenar los datos de la partida        