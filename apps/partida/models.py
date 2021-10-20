from django.db import models

#Modelo para almacenar los jugadores de la partida    
class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)

class Partida(models.Model):
    codigo_ingreso = models.CharField(max_length=5)

class Anotacion(models.Model):
    jugador = models.ForeignKey(Jugadores, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
 
#Modelo para almacenar los datos de la partida        