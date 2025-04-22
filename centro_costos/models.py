from django.db import models
from django.db import models
from partidas_planos.models import User

class CentroDeCostos(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoDeGasto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Actividad(models.Model):
    TIPO = [
        ('Por separado', 'Por separado'),
        ('A todo costo', 'A todo costo'),
    ]

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    centro_de_costos = models.ForeignKey(CentroDeCostos, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO)
    responsable = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    detalle = models.TextField()
    documento = models.CharField(max_length=100)
    debe = models.DecimalField(max_digits=10, decimal_places=2)
    haber = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_gasto = models.ForeignKey(TipoDeGasto, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
