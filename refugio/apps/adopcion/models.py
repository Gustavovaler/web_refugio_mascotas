from django.db import models
from django.urls import reverse

'''Modelo o tabla Persona. '''

class Persona(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=20)
	email = models.EmailField()
	domicilio = models.TextField()
    
    #este metodo retorna un nombre verboso para ver los objetos Persona

	def __str__(self):
		return self.nombre
    
    # este metodo proporciona la redireccion una vez echa una modificacion o alta.
    
	def get_absolute_url(self):
		return reverse('personalist')



