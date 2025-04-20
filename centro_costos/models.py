from django.db import models
from django.db import models
from partidas_planos.models import User

class Responsable(models.Model):
    documento = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

class Proyecto(models.Model):
    TIPO_GASTO_CHOICES = [
        ('Por separado', 'Por separado'),
        ('A todo costo', 'A todo costo'),
    ]

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    centro_de_costos = models.CharField(max_length=100) ####
    tipo_gasto = models.CharField(max_length=20, choices=TIPO_GASTO_CHOICES)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)


class Actividad(models.Model):

    ADICIONAL_CHOICES = [
        ('si', 'SI'),
        ('no', 'NO'),
    ]

    nombre_actividad = models.CharField(max_length=100)
    codigo_actividad = models.CharField(max_length=50)
    adicional = models.CharField(max_length=5, choices=ADICIONAL_CHOICES)
    tipo_gasto = models.CharField(max_length=100) ###
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_actividad


class Gasto(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    fecha = models.DateField()
    detalle = models.TextField()
    documento = models.CharField(max_length=100)
    # debe = models.DecimalField(max_digits=10, decimal_places=2)
    # haber = models.DecimalField(max_digits=10, decimal_places=2)
    # saldo = models.DecimalField(max_digits=10, decimal_places=2)
    sustento = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gasto #{self.id} - {self.item}"
