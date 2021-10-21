from django import forms
from django.contrib.auth.models import User
from apps.partida.models import Partida, Jugador
class jugador_form(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
        exclude =['usuario']


class crear_partida_form(forms.ModelForm):
   class Meta:
       model = Partida
       fields = '__all__'
       exclude=['codigo_ingreso']




class ingresar_partida_form(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        

class registro_form(forms.Form):
    username   = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    clave_1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=False))
    clave_2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            c = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El usuario ingresado, ya se encuentra registrado')

    def clean_clave_2(self):
        clave_1 = self.cleaned_data['clave_1']
        clave_2 = self.cleaned_data['clave_2']
        if clave_1 == clave_2:
            return clave_2
        else:
            raise forms.ValidationError('Las contraseñas no coinciden, intente de nuevo')

class login_form(forms.Form):
    username   = forms.CharField(label='Usuario', widget=forms.TextInput)
    clave = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=False))