from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=50,verbose_name='Marca')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'
        ordering=['-marca']

    def __str__(self):
        return self.marca

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=20,verbose_name='ID')
    descripcion = models.CharField(max_length=255,verbose_name="Descripción")
    precio_unitario = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,null=True,blank=True)
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['idProducto']

    def __str__(self):
        return self.descripcion