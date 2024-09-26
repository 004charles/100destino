from django.urls import path
from . import views  


urlpatterns = [
    path('transportadoras/', views.transportadoras, name='transportadoras'), 
   
]
