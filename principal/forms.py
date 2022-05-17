from socket import fromshare
from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            "id_persona",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "gmail",
            "contraseña",
            "telefono",
            "edad",
            "fecha_nacimiento",
            "fecha_ingreso",
        ]