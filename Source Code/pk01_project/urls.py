"""pk01_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postulantes01 import views

urlpatterns = [
    path('', views.buscar_postulante, name='index'),  # Página principal
    path('buscar_postulante/', views.buscar_postulante, name='buscar_postulante'),
    path('admin/', admin.site.urls),
    path('informacion-admision/', views.informacion_admision, name='informacion_admision'),
    path('desistir_cupo/<str:rut>/', views.desistir_cupo, name='desistir_cupo'),
    path('confirmar_admision/<str:rut>/', views.confirmar_admision, name='confirmar_admision'),
    path('proceder_admision/<str:rut>/', views.proceder_admision, name='proceder_admision'),
    # Rutas para las páginas de confirmación exitosa 
    path('admitido-confirmacion-exitosa/', views.admitido_confirmacion_exitosa, name='admitido_confirmacion_exitosa'),
    path('lista-confirmacion-exitosa/', views.lista_confirmacion_exitosa, name='lista_confirmacion_exitosa'),
]

