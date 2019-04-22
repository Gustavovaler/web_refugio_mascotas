from django.db import models
from django.urls import reverse


class Persona(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=20)
	email = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('personalist')



