from django.db import models

class postulante_pk2025(models.Model):
    ESTADOS = [
        ('admitido', 'Admitido'),
        ('lista_espera', 'Lista de Espera'),
        ('no_admitido', 'No Admitido'),
        ('desistido', 'Desistido'),
    ]

    GENEROS = [
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    ]

    CONFIRMACION_CHOICES = [
        ('confirmado', 'Confirmado'),
        ('negado', 'Negado'),
        ('', '')
    ]

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    motivo_desistimiento = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=GENEROS)
    posicion_lista_espera = models.IntegerField(blank=True, null=True)
    colegio_alternativo = models.TextField(blank=True, null=True)
    confirmacion = models.CharField(max_length=20, choices=CONFIRMACION_CHOICES, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.estado}"
