from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home (request):
	return render(request, 'core/home.html')

def colaboradores (request):
	return  render (request, 'core/colaboradores.html')

def informaciontienda (request):
	return  render (request, 'core/informaciontienda.html')

def carritodecompras (request):
	return  render (request, 'core/carritodecompras.html')

def accesoriosperros (request):
	return  render (request, 'core/accesoriosperros.html')

def accesoriosgatos (request):
	return  render (request, 'core/accesoriosgatos.html')

