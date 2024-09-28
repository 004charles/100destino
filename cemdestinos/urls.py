from django.contrib import admin
from django.urls import path, include
from usuarios import views  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index, name="index"),  # A URL para a view index
    path('100destino/', include('usuarios.urls')), 
    
]
