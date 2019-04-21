from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Mascota
from apps.adopcion.models import Persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request



def index(request):
	return HttpResponse(render(request,template_name = 'index.html'))


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
		


