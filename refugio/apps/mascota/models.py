from django.db import models
from apps.adopcion.models import Persona
from django.urls import reverse


class Vacuna(models.Model):
	nombre = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('mascotalist')

	def __str__(self):
		return self.nombre 
		
class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna,blank=True)

	def __str__(self):		
		return self.nombre

	def get_absolute_url(self,**kwargs):
		return reverse('mascotalist')

	class Meta:
		"""docstring for Meta"""
		verbose_name='Mascota'
		

		