from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, View
from .models import Mascota, Vacuna, UserNew
from apps.adopcion.models import Persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


#vista de funcion para la landing page. A mejorar en un futuro proximo

def index(request):
	return HttpResponse(render(request,template_name = 'index.html'))

# vista  para listar todas las mascotas
class MascotaList(LoginRequiredMixin, ListView):
	login_url = '/accounts/login/'
	model = Mascota
	template_name='mascotalist.html'

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data()
		context['mascotaslist'] = Mascota.objects.all()
		return context

class PersonaDetail(LoginRequiredMixin, DetailView):
	login_url = '/accounts/login/'
	model = Persona
	template_name = 'personadetail.html'

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data()
		return context

class MascotaCrear(LoginRequiredMixin, CreateView):
	login_url = '/accounts/login/'
	model = Mascota
	template_name = 'mascotacreate.html'
	fields = '__all__'

class PersonaList( LoginRequiredMixin, ListView):
	login_url = '/accounts/login/'
	model = Persona
	template_name = 'personalist.html'
	"""docstring for PersonaList"""
	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['personas'] = Persona.objects.all()
		return context
		

class VacunaCreate(LoginRequiredMixin,CreateView):
	login_url = ('/accounts/login/')
	model = Vacuna
	template_name = 'nueva_vacuna.html'
	fields = ['nombre']

class MascotaDetail(LoginRequiredMixin,DetailView):
	login_url = '/accounts/login/'
	model = Mascota
	template_name = 'mascota_detail.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data()
		return context


class MascotaUpdate(LoginRequiredMixin,UpdateView):
	login_url = ('/account/login/')
	model = Mascota
	fields = '__all__'
	template_name = 'mascota_update_form.html'
	template_name_suffix = '_update_form'

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		return context

class PersonaUpdate(LoginRequiredMixin, UpdateView):
	login_url = ('/account/login/')
	model = Persona
	fields = '__all__'
	template_name = 'persona_update_form.html'
	template_name_suffix = '_update_form'

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		return context

class PersonaCreate(LoginRequiredMixin, CreateView):
	login_url = '/accounts/login/'
	model = Persona
	template_name = 'nueva_persona.html'
	fields = '__all__'

class UserCreate(UserNew, CreateView):
	model = UserNew
	template_name = 'registration/registro_usuario.html'
	fields = ['first_name',
	          'last_name',
	          'email',
	          'username',
	          'password',
	          ]



	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		print(UserNew.password)
		return context





	



