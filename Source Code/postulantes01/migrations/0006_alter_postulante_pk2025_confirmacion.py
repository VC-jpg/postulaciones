# Generated by Django 5.0.4 on 2024-04-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes01', '0005_alter_postulante_pk2025_colegio_alternativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante_pk2025',
            name='confirmacion',
            field=models.CharField(blank=True, choices=[('confirmado', 'Confirmado'), ('negado', 'Negado'), ('', '')], max_length=20),
        ),
    ]