from django.contrib import admin
from apps.partida.models import Partida, Jugador, Registro, Turno

admin.site.register(Partida),
admin.site.register(Jugador),
admin.site.register(Registro),
admin.site.register(Turno),
