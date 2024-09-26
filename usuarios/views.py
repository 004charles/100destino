from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def transportadoras(request):
    return render(request, 'transportadoras.html')