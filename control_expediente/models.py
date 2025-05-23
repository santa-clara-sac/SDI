from django.db import models
from django.utils import timezone
from partidas_planos.models import User

class CasoJudicial(models.Model):
    REPRESENTANTE_CHOICES = [
        ('demandante', 'Demandante'),
        ('demandado', 'Demandado'),
    ]
    codigo = models.CharField(max_length=100, blank=True, null=True)
    expediente = models.CharField(max_length=100)
    sede = models.CharField(max_length=100, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    materia = models.CharField(max_length=100, blank=True, null=True)
    juzgado = models.CharField(max_length=100, blank=True, null=True)
    demandante = models.CharField(max_length=255)
    demandado = models.CharField(max_length=255)
    anio_inicio = models.CharField(max_length=4, blank=True, null=True)
    representante = models.CharField(max_length=20, choices=REPRESENTANTE_CHOICES)
    tlf_juzgado = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # return f"{self.expediente} - {self.demandante} vs {self.demandado}"
        return f"{self.expediente}"


class Seguimiento(models.Model):
    ESTADO_CHOICES = [
        ('En proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
        ('Presentado', 'Presentado'),
        ('Notificado', 'Notificado'),
    ]

    caso = models.ForeignKey(CasoJudicial, on_delete=models.CASCADE, related_name='seguimientos')
    resolucion = models.CharField(max_length=255, blank=True, null=True)
    fecha_seguimiento = models.DateField(blank=True, null=True)
    seguimiento = models.TextField()
    fecha_pendiente = models.DateField(blank=True, null=True) # fecha notificacion
    pendiente = models.TextField(blank=True)
    responsable = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_proceso')
    pdf = models.FileField(upload_to='seguimiento/', blank=True, null=True)
    # inter = models.BooleanField(default=False)
    inter = models.BooleanField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now=True) # (auto_now_add=True)
    editor = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='seguimientos_creados')    

    def __str__(self):
        return f"Seguimiento - {self.caso.expediente} - {self.fecha_seguimiento}"



class Gasto(models.Model):
    seguimiento = models.ForeignKey(Seguimiento, on_delete=models.CASCADE, related_name='gastos')
    fecha = models.DateField()
    detalle = models.TextField()
    sustento = models.TextField(blank=True)
    pdf = models.FileField(upload_to='gastos_expediente/', blank=True, null=True)
    codigo_pago = models.CharField(max_length=255, blank=True, null=True)
    gastos_soles = models.DecimalField(max_digits=10, decimal_places=2)
    gastos_dolares = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Gasto - {self.seguimiento.caso.expediente} - {self.fecha}"

################################################################################################################

class Presentacion(models.Model):
    caso = models.ForeignKey(CasoJudicial, on_delete=models.CASCADE, related_name='presentaciones')
    fecha = models.DateField()
    presentado = models.TextField()
    escrito = models.CharField(max_length=255)

    def __str__(self):
        return f"Seguimiento - {self.caso.expediente} - {self.fecha}"



class GastoPresentacion(models.Model):
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE, related_name='gastos_presentaciones')
    fecha = models.DateField()
    detalle = models.TextField()
    sustento = models.TextField(blank=True)
    pdf = models.FileField(upload_to='gastos_expediente/', blank=True, null=True)
    gastos_soles = models.DecimalField(max_digits=10, decimal_places=2)
    gastos_dolares = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Gasto - {self.presentacion.caso.expediente} - {self.fecha}"  # Corregido aquí
