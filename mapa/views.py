from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ubicacion, TicketBarrera # ¡Aquí estaba el error! Cambiamos Edificio por Ubicacion

# 1. LA FUNCIÓN QUE CARGA EL MAPA
def inicio(request):
    edificios = Ubicacion.objects.all() # Y aquí también pedimos a Ubicacion en vez de Edificio
    return render(request, 'mapa/inicio.html', {'edificios': edificios})

# 2. LA FUNCIÓN DEL REPORTE
def reportar(request):
    if request.method == 'POST':
        lugar_form = request.POST.get('lugar')
        tipo_form = request.POST.get('tipo_barrera')
        desc_form = request.POST.get('descripcion')

        nuevo_reporte = TicketBarrera(
            lugar=lugar_form,
            tipo_barrera=tipo_form,
            descripcion=desc_form
        )
        nuevo_reporte.save()
        return redirect('inicio')
    
    return redirect('inicio')