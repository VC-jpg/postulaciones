from django.shortcuts import render, redirect
from .models import postulante_pk2025
from .forms import PostulanteForm
from django.http import JsonResponse

def admitido_confirmacion_exitosa(request):
    return render(request, 'Admitido_confirmacion_exitosa.html')

def lista_confirmacion_exitosa(request):
    return render(request, 'Lista_confirmacion_exitosa.html')

def informacion_admision(request):
    return render(request, 'informacion-admision.html')

def buscar_postulante(request):
    if request.method == 'POST':
        form = PostulanteForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            try:
                postulante = postulante_pk2025.objects.get(rut=rut)
                # Redirigir según el estado del postulante!!!!
                if postulante.estado == "admitido" and postulante.confirmacion == "confirmado":
                    return render(request, 'Admitido_confirmacion_exitosa.html', {'postulante': postulante})
                elif postulante.estado == "lista_espera" and postulante.confirmacion == "confirmado":
                    return render(request, 'Lista_confirmacion_exitosa.html', {'postulante': postulante})
                else:
                    return render(request, 'resultado.html', {'postulante': postulante})
            except postulante_pk2025.DoesNotExist:
                mensaje = "El RUT ingresado no se encuentra registrado, verifique bien si ingresó el RUT correctamente."
                return render(request, 'error.html', {'mensaje': mensaje})
    else:
        form = PostulanteForm()
    return render(request, 'buscar_postulante.html', {'form': form})


def desistir_cupo(request, rut):
    if request.method == 'POST':
        motivo = request.POST.get('motivo_desistimiento')
        colegio_alternativo = request.POST.get('colegio_alternativo')  
        if motivo:
            try:
                postulante = postulante_pk2025.objects.get(rut=rut)
                postulante.estado = 'desistido'
                postulante.confirmacion = 'negado' 
                postulante.motivo_desistimiento = motivo
                postulante.colegio_alternativo = colegio_alternativo 
                postulante.save()
                return redirect('buscar_postulante')
            except postulante_pk2025.DoesNotExist:
                mensaje = "El postulante no existe."
        else:
            mensaje = "El motivo de desistimiento no fue proporcionado."
    else:
        mensaje = "El formulario de desistimiento no fue enviado correctamente."
    return render(request, 'resultado.html', {'mensaje': mensaje})


def confirmar_admision(request, rut):
    if request.method == 'POST':
        try:
            postulante = postulante_pk2025.objects.get(rut=rut)
            postulante.confirmacion = 'confirmado'
            postulante.save()
            return JsonResponse({'message': 'Confirmación exitosa'}, status=200)
        except postulante_pk2025.DoesNotExist:
            return JsonResponse({'error': 'El postulante no existe'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def proceder_admision(request, rut):
    if request.method == 'POST':
        try:
            postulante = postulante_pk2025.objects.get(rut=rut)
            postulante.confirmacion = 'confirmado'
            postulante.save()
            return JsonResponse({'message': 'Confirmación exitosa'}, status=200)
        except postulante_pk2025.DoesNotExist:
            return JsonResponse({'error': 'El postulante no existe'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
