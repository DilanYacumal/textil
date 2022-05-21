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
            "correo_electronico",
            "contraseña",
            "telefono",
            "edad",
            "fecha_nacimiento",
            "fecha_ingreso",
            "tipo_persona_idtipo_persona",
            "area_idarea",
            "tipo_documento_idtipo_documento",
        ]