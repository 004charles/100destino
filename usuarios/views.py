from django.shortcuts import render
from .models import Companhia, Usuario
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages




def index(request):
    return render(request, 'index.html')  

def transportadoras(request):
    return render(request, 'transportadoras.html')


def login_transporte(request):
    return render(request, 'login_transporte.html')


def transporte(request):
    if 'companhia' in request.session:
        companhia_id = request.session['companhia']
        companhia = Companhia.objects.get(id=companhia_id)
        return HttpResponse("Bem vindo")
    else:
        return HttpResponse("Você não está autenticado para acessar esta página.")


from django.shortcuts import redirect

def valida_login_transporte(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    companhia = Companhia.objects.filter(email=email, senha=senha)
    
    if not companhia.exists():
        messages.error(request, "E-mail ou senha incorretos.") 
        return redirect('usuarios:login_transporte')  
    
    # Se houver um resultado, faça o login
    request.session['companhia'] = companhia[0].id
    return redirect('usuarios:conta_agencia')  # Redireciona para a página principal

def valida_login_admin(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuarios = Usuario.objects.filter(email=email, senha=senha)
    
    if not usuarios.exists():
        messages.error(request, "E-mail ou senha incorretos.")  
        return redirect('usuarios:login_admin')  
    
    request.session['usuarios'] = usuarios[0].id
    return redirect('usuarios:adminOs')

def login_admin(request):
    return render(request, 'conta_admin.html')


def admin(request):
    return render(request, 'admin.html')

def conta_agencia(request):
    return render(request, 'conta_agencia.html')

def viagem_agencia(request):
    return render(request, 'viagem_agencia.html')

def pagamento(request):
    return render(request, 'pagamento.html')

def Ango(request):
    return render(request, 'ango.html')

def huambo(request):
    return render(request, 'huamboexpress.html')