from django.urls import path
from . import views  

app_name = 'usuarios'  

urlpatterns = [
    path('', views.index, name='index'),  # Adicione a view index aqui
    path('transportadoras/', views.transportadoras, name='transportadoras'), 
    path('login_transporte/', views.login_transporte, name='login_transporte'),
    path('valida_login_transporte/', views.valida_login_transporte, name='valida_login_transporte'),
    path('transporte/', views.transporte, name='transporte'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('valida_login_admin/', views.valida_login_admin, name='valida_login_admin')
]
