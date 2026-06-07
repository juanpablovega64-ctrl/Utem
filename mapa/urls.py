from django.urls import path
from . import views

urlpatterns = [
    # Tu ruta normal del inicio
    path('', views.inicio, name='inicio'),
    
    # NUEVA RUTA PARA EL REPORTE
    path('reportar/', views.reportar, name='reportar'),
]