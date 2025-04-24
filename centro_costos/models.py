from django.db import models
from django.db import models
from partidas_planos.models import User
from django.core.validators import MaxLengthValidator

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
    #nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    detalle = models.TextField()
    documento = models.CharField(max_length=100, blank=True, null=True)
    debe = models.DecimalField(max_digits=10, decimal_places=2)
    haber = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_gasto = models.ForeignKey(TipoDeGasto, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detalle

class CantaCallao(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    concepto = models.CharField(max_length=100)
    detalle = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(100)])
    referencia = models.CharField(max_length=100, blank=True, null=True)
    # monto1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # monto2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto1 =  models.CharField(max_length=10, blank=True, null=True)
    monto2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.detalle[:30]}"

#####################################################################################################

class GastoGeneral(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.FileField(upload_to='gastos', blank=True, null=True, max_length=255)
    monto_soles = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    monto_dolares = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    actividad = models.CharField(max_length=255, blank=True, null=True)
    tipo_gasto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.detalle[:50]}" if self.codigo and self.detalle else "Gasto General"