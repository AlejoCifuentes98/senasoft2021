from django import forms
from apps.partida.models import Partida, Jugador
class jugador_form(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'


class crear_partida_form(forms.ModelForm):
   class Meta:
       model = Partida
       fields = '__all__'
       exclude=['codigo_ingreso']




class ingresar_partida_form(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        
