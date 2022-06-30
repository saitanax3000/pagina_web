from operator import index
from turtle import home
from django.urls import path
from .views import *

urlpatterns = [
	path ('', home,name="home"),
	path ('colaboradores/', colaboradores,name="colaboradores"),
	path ('informaciontienda/' , informaciontienda,name="informaciontienda"),
	path ('carritodecompras/', carritodecompras,name="carritodecompras"),
	path ('accesoriosperros/', accesoriosperros,name="accesoriosperros"),
	path ('accesoriosgatos/', accesoriosgatos,name="accesoriosgatos"),

]
