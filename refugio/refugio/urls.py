"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.mascota import views
from apps.mascota.views import MascotaList, MascotaDetail, MascotaUpdate, PersonaUpdate, UserCreate
from apps.mascota.views import PersonaDetail, MascotaCrear, PersonaList, VacunaCreate, PersonaCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/int:<pk>', MascotaDetail.as_view(),name = 'mascotadetail'),
    path('mascota_modificar/int:<pk>', MascotaUpdate.as_view(), name = 'mascotaupdate'),
    path('mascota',MascotaList.as_view(),name='mascotalist'),
    path('nuevo_usuario', UserCreate.as_view(), name = 'usuariocreate'),
    path('persona_modificar/<pk>', PersonaUpdate.as_view(), name =  'personaupdate'),
    path(r'persona/<int:pk>',PersonaDetail.as_view(), name='personadetail'),
    path('nueva_persona', PersonaCreate.as_view(), name = 'personacreate'),
    path('nueva_mascota', MascotaCrear.as_view(),name='nueva_mascota'),
    path('lista_personas' , PersonaList.as_view(), name = 'personalist'),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('vacuna', VacunaCreate.as_view(), name = 'nueva_vacuna'),
    path('', views.index, name = 'index'),
]  
