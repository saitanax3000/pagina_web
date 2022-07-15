from rest_framework import serializers
from crud.models import Producto, Marca

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto','descripcion','precio_unitario','stock','marca','created_at','updated_at')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id','marca')
