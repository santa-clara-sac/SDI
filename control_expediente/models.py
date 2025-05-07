from django.db import models

class CasoJudicial(models.Model):
    REPRESENTANTE_CHOICES = [
        ('demandante', 'Demandante'),
        ('demandado', 'Demandado'),
    ]

    codigo = models.PositiveIntegerField()
    expediente = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    juzgado = models.CharField(max_length=100)
    demandante = models.CharField(max_length=255)
    demandado = models.CharField(max_length=255)
    anio_inicio = models.CharField(max_length=4, blank=True, null=True)
    representante = models.CharField(
        max_length=20,
        choices=REPRESENTANTE_CHOICES
    )

    def __str__(self):
        return f"{self.expediente} - {self.demandante} vs {self.demandado}"