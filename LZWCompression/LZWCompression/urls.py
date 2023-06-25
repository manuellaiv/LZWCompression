"""
URL configuration for LZWCompression project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('encode/', views.encode_view, name='encode'),
    path('decode/', views.decode_view, name='decode'),
    path('get-all/', views.get_all_view, name='get-all'),
    path('get-all-inp/', views.get_all_inp_view, name='get-all-inp'),
    path('get-all-out/', views.get_all_out_view, name='get-all-out'),
    path('get-all-status/', views.get_all_status_view, name='get-all-status')
]
