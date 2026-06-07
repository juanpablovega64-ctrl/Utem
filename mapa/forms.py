from django import forms
from .models import ReporteBarrera

class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteBarrera
        # Solo le pedimos al usuario que elija el punto malo y describa el problema
        fields = ['punto_afectado', 'descripcion']
        
        # Le ponemos clases de Bootstrap para que se vea moderno
        widgets = {
            'punto_afectado': forms.Select(attrs={'class': 'form-select mb-3'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 3, 'placeholder': 'Ej: La rampa está bloqueada por unas sillas...'}),
        }