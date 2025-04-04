from django.db import models

# Create your models here.
class Frutas(models.Model):
    # Definimos los campos del modelo Frutas
    # Se utiliza la clase models.Field para definir los campos del modelo
    nombre: models.Field = models.CharField(max_length=30) # Definimos el campo nombre como un CharField con un máximo de 30 caracteres
    precio: models.Field = models.DecimalField(max_digits=5 ,decimal_places=2) # Definimos el campo precio como un DecimalField con un máximo de 5 dígitos y 2 decimales
    distribuidora: models.Field = models.CharField(max_length=60) # Definimos el campo distribuidora como un CharField con un máximo de 60 caracteres

    # Definimos el método __str__ para representar el objeto de tipo Frutas como una cadena de texto
    # El método __str__ se utiliza para representar el objeto de tipo Frutas como una cadena de texto
    # Este tipo de métodos se les llama métodos de doble guion bajo o métodos mágicos
    # Estos métodos se utilizan para definir el comportamiento de los objetos para realizar ciertas operaciones
    # como __str__, __repr__, __add__, __sub__, etc.
    def __str__(self):
        return f"{self.nombre} {self.distribuidora} con precio {self.precio}"
    