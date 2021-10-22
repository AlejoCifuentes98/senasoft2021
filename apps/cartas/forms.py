from django import forms
from .models import Cartas

tipo_turno = (
    ('preguntar','preguntar'),
    ('acusar','acusar'),)
    
class turno_form(forms.Form):
    desa = forms.ModelChoiceField(label='Desarrollador',queryset= Cartas.objects.filter(tipo__nombre = "desarrollador"))
    erro = forms.ModelChoiceField(label='Error',queryset= Cartas.objects.filter(tipo__nombre = "error"))
    modu = forms.ModelChoiceField(label='Modulo',queryset= Cartas.objects.filter(tipo__nombre = "modulo"))
    tipo = forms.ChoiceField(choices=tipo_turno, label='Tipo de jugada')