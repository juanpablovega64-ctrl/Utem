from django.db import models
from django.contrib.auth.models import User

class Ubicacion(models.Model):
    TIPO_CHOICES = [
        ('edificio', 'Edificio'),
        ('sala', 'Sala de Clases'),
        ('zona_tranquila', 'Zona Tranquila'),
        ('entrada_principal', 'Entrada Principal'),
        ('entrada_secundaria', 'Entrada Secundaria'),
        ('rampa', 'Rampa de Acceso'), 
        ('banio', 'Baño Accesible'), # Y aprovecha de agregar el del baño aquí para que te salga en el admin
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.CharField(max_length=50, null=True, blank=True)
    longitud = models.CharField(max_length=50, null=True, blank=True)
    
    foto = models.ImageField(upload_to='ubicaciones/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class PuntoAccesibilidad(models.Model):
    TIPO_CHOICES = [
        ('ascensor', 'Ascensor'),
        ('rampa', 'Rampa'),
        ('bano', 'Baño Accesible'),
    ]
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='puntos_accesibilidad')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    esta_disponible = models.BooleanField(default=True)
    
    def __str__(self):
        estado = "Disponible" if self.esta_disponible else "No Disponible"
        return f"{self.tipo} en {self.ubicacion.nombre} - {estado}"

class ReporteBarrera(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    punto_afectado = models.ForeignKey(PuntoAccesibilidad, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)

    def __str__(self):
        estado = "Resuelto" if self.resuelto else "Pendiente"
        return f"Reporte en {self.punto_afectado} ({estado})"

class DestinoFrecuente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Destino de {self.usuario.username}: {self.ubicacion.nombre}"
class TicketBarrera(models.Model):
    lugar = models.CharField(max_length=150)
    tipo_barrera = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)

    def __str__(self):
        estado = "✅ Resuelto" if self.resuelto else "🚨 Pendiente"
        return f"[{estado}] {self.tipo_barrera} en {self.lugar}"