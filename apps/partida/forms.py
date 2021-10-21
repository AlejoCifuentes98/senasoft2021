from django import forms
from apps.partida.models import Partida, Turno
from apps.cartas.models import Cartas
from django.contrib.auth.models import User
tipo_turno = (
    ('preguntar','preguntar'),
    ('acusar','acusar'),)


class crear_partida_form(forms.ModelForm):
   class Meta:
       model = Partida
       fields = '__all__'
       exclude=['codigo_ingreso']

class register_form(forms.Form):
    username   = forms.CharField(label='Apodo', widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            c = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El correo ingresado, ya se encuentra registrado')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError('Las contraseñas no coinciden, intente de nuevo')

class login_form(forms.Form):
    nombre   = forms.CharField(label='Nombre', widget=forms.TextInput)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=False))

class ingresar_partida_form(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        
class turno_form(forms.Form):
    desa = forms.ModelChoiceField(label='Desarrollador',queryset= Cartas.objects.filter(tipo__nombre = "dev"))
    erro = forms.ModelChoiceField(label='Error',queryset= Cartas.objects.filter(tipo__nombre = "err"))
    modu = forms.ModelChoiceField(label='Modulo',queryset= Cartas.objects.filter(tipo__nombre = "mod"))
    tipo = forms.ChoiceField(choices=tipo_turno, label='Tipo de jugada')

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
