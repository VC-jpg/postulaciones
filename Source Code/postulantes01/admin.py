# /django-project/src/postulantes01/admin.py
from django.contrib import admin
from .models import postulante_pk2025


class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'estado', 'genero', 'posicion_lista_espera', 'colegio_alternativo', 'confirmacion')
    list_filter = ('estado', 'confirmacion', 'genero')
    search_fields = ['rut', 'nombre']

admin.site.register(postulante_pk2025, PostulanteAdmin)
