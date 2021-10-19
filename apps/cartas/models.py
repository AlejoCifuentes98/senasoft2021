from django.db import models


class Tipo(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre)

class Cartas(models.Model):
    nombre = models.CharField(max_length=80)
    tipo   = models.ForeignKey()
    def __str__(self):
        return str(self.nombre)
