
from django.shortcuts import render,redirect,reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/product_list.html',context)

@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio_unitario = form.cleaned_data.get("precio_unitario")
            stock = form.cleaned_data.get("stock")
            marca = form.cleaned_data.get("marca")
            imagen = form.cleaned_data.get("imagen")
            obj = Producto.objects.create(
                idProducto=idProducto,
                descripcion=descripcion,
                precio_unitario=precio_unitario,
                stock=stock,
                marca=marca,
                imagen=imagen
            )
            obj.save()
            return redirect(reverse('product-list')+"?OK")
        else:
            return redirect(reverse('product-list')+"?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/product_new.html',{'form':form})

def product_detail(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product_detail.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")

@login_required
def product_edit(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            form = ProductoForm(instance=producto)
        else:
            return redirect(reverse('product-list') + "?FAIL")

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('product-list') + "?SUCCESS")
            else:
                return redirect(reverse('product-edit') + product_id)
        context = {'form':form}
        return render(request,'crud/product_edit.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('product-list') + "?DELETED")
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_by_marca(request,marca):
    productos = Producto.objects.filter(marca=marca)
    return render(request,'crud/product_list.html',{'productos':productos})
