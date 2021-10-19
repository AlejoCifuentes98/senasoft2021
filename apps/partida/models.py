from django.db import models

#Modelo para almacenar los jugadores de la partida    
class Jugadores(models.Model):
    nombre = models.Charfield(max_length=100)

#Modelo para almacenar los datos de la partida        
class Partida(models.Model):
    jugadores = models.ForeignKey(Jugadores, ondelete=models.CASCADE)