from django.contrib import admin
from .models import Ubicacion, PuntoAccesibilidad, TicketBarrera

# Registramos todos los modelos para que aparezcan en el panel
admin.site.register(Ubicacion)
admin.site.register(PuntoAccesibilidad)
admin.site.register(TicketBarrera)