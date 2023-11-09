from django.urls import path, include
from galeria.views import index, imagem
from django.contrib import admin

urlpatterns = [
    path('', index),
    path('imagem.html/', imagem),
    #path("admin/", admin.site.urls)
      
]
