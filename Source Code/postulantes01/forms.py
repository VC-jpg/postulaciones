from django import forms
from .models import postulante_pk2025

class PostulanteForm(forms.Form):
    rut = forms.CharField(label='Ingrese su RUT', max_length=12)

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        # Realiza cualquier validación adicional del RUT aquí si es necesario
        return rut
