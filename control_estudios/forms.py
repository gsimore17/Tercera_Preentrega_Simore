from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.IntegerField(required=True, max_value=50000000)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True, max_value=5000000)
    fecha_nacimiento = forms.CharField(required=True, max_length=64)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.IntegerField(required=True, max_value=50000000)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.CharField(required=True, max_length=64)
    profesion = forms.CharField(required=True, max_length=64)
    
