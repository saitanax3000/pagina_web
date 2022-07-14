from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'descripcion',
            'precio_unitario',
            'stock',
            'marca',
            'imagen'
        ]
        labels = {
            'idProducto':'Código Producto',
            'descripcion':'Descripción',
            'precio_unitario':'Precio Unitario',
            'stock':'Stock',            
            'marca':'Marca',
            'imagen':'Imagen',            
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }