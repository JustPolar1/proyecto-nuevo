from django.db import models

# Create your models here.
class Frutas(models.Model):
    nombre: models.Field = models.CharField(max_length=30)
    precio: models.Field = models.DecimalField(max_digits=5 ,decimal_places=2)
    distribuidora: models.Field = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre} {self.distribuidora} con precio {self.precio}"
    