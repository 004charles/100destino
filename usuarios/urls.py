from django.urls import path
from . import views  

app_name = 'usuarios'  

urlpatterns = [
    path('', views.index, name='index'),  # Adicione a view index aqui
    path('transportadoras/', views.transportadoras, name='transportadoras'), 
    path('login_transporte/', views.login_transporte, name='login_transporte'),
    path('valida_login_transporte/', views.valida_login_transporte, name='valida_login_transporte'),
    path('transporte/', views.transporte, name='transporte'),
    path('pagamento/', views.pagamento, name='pagamento'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('adminOs/', views.admin, name='adminOs'),
    path('ango/', views.Ango, name='ango'),
    path('huambo/', views.huambo, name='huambo'),
    path('conta_agencia/', views.conta_agencia, name='conta_agencia'),
    path('viagem_agencia/', views.viagem_agencia, name='viagem_agencia'),
    path('valida_login_admin/', views.valida_login_admin, name='valida_login_admin')
]
