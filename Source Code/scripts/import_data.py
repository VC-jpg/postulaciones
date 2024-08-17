import pandas as pd
import os
import sys
import django
from django.db import IntegrityError

# Agrega la ruta de tu proyecto Django al path de Python
sys.path.append('/django-project/src')

# Configura la variable de entorno para el proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pk01_project.settings')

# Asegúrate de que Django esté cargado antes de importar los modelos
django.setup()

# Importa el modelo desde tu aplicación
from postulantes01.models import postulante_pk2025

def main():
    # Ruta al archivo CSV
    csv_file = '/django-project/src/data/Listado Admisiones Estados PK2025.csv'

    # Leer el archivo CSV con el delimitador ';' especificado
    df = pd.read_csv(csv_file, sep=';')

    # Imprimir los encabezados del DataFrame
    print("Encabezados del archivo CSV:")
    print(df.columns)

    # Iterar sobre cada fila del DataFrame y guardar o actualizar los datos en la base de datos
    for index, row in df.iterrows():
        rut = row['rut']

        # Manejar valores NaN en 'posicion_lista_espera'
        if pd.isna(row['posicion_lista_espera']):
            row['posicion_lista_espera'] = None  # Convertir NaN a None

        # Obtener el motivo de desistimiento (nulo si no está presente)
        motivo_desistimiento = row.get('Motivo_Desistimiento', None)

        # Obtener el colegio alternativo (nulo si no está presente)
        colegio_alternativo = row.get('Colegio_Alternativo', None)

        # Buscar si el registro ya existe en la base de datos
        try:
            postulante = postulante_pk2025.objects.get(rut=rut)

            # Actualizar los campos necesarios
            postulante.nombre = row['nombre']
            postulante.estado = row['estado']
            postulante.genero = row['genero']
            postulante.posicion_lista_espera = row['posicion_lista_espera']
            postulante.motivo_desistimiento = motivo_desistimiento
            postulante.colegio_alternativo = colegio_alternativo
            postulante.save()
            print(f"Registro actualizado para rut: {rut}")
        except postulante_pk2025.DoesNotExist:
            # Si el registro no existe, crear uno nuevo
            try:
                postulante = postulante_pk2025.objects.create(
                    rut=rut,
                    nombre=row['nombre'],
                    estado=row['estado'],
                    genero=row['genero'],
                    posicion_lista_espera=row['posicion_lista_espera'],
                    motivo_desistimiento=motivo_desistimiento,
                    colegio_alternativo=colegio_alternativo
                )
                print(f"Nuevo registro creado para rut: {rut}")
            except IntegrityError as e:
                print(f"Error al crear el registro para rut {rut}: {e}")

if __name__ == "__main__":
    main()
