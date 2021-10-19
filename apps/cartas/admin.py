from django.contrib import admin
from .models import Cartas, Tipo
# Register your models here.
admin.site.register(Cartas, Tipo)