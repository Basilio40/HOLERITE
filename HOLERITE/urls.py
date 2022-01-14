"""HOLERITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from core.api import viewsets

route = routers.DefaultRouter()
route.register('funcionario', viewsets.FuncionarioViewSets, basename='funcionario')
route.register('holerite', viewsets.HoleriteViewSets, basename='holerite')
route.register('filepdf', viewsets.FilePdfViewSets, basename='filepdf')
route.register('ponto', viewsets.PontoViewSets, basename='ponto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
