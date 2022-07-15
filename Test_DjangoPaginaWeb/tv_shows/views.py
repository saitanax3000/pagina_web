from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import *
from django.contrib import messages

# Create your views here.
def shows(request):
    if 'usuario' not in request.session:
        return redirect("/")

    context = {
        'shows':Show.objects.all(),
    }
    return render(request,'tv_shows/shows.html',context)

def new(request):
    context = {
        'networks':Network.objects.all(),
    }
    return render(request,'tv_shows/new.html',context)

def create(request):
    if request.method == 'GET':
        return redirect('/new')
    elif request.method == 'POST':
        # pasar los datos al método que escribimos y guardar la respuesta en una variable llamada errores
        errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            
            # redirigir al usuario al formulario para corregir los errores
            return redirect(reverse('new'))
        else:
            title = request.POST['title']
            description = request.POST['description']
            network_id = request.POST['network']
            network = Network.objects.get(id=network_id)
            release_date = request.POST['release_date']
            obj = Show.objects.create(title=title, description=description, network=network, release_date=release_date)
            obj.save()
            #messages.success(request, "Show successfully created")
            return redirect(f"/shows/{obj.id}")

def info_show(request, show_id):
    context = {
        'show':Show.objects.get(id=show_id),
        #'show':get_object_or_404(Show,show_id)
    }
    return render(request, 'tv_shows/info_show.html', context)

def edit_show(request, show_id):
    context = {
        'show':Show.objects.get(id=show_id),
        'networks':Network.objects.all(),
    }
    return render(request, 'tv_shows/edit.html', context)

def update(request, show_id):
    if request.method == 'GET':
        return redirect(f'/shows/{show_id}/edit')
    elif request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_network_id = request.POST['network']
        new_network = Network.objects.get(id=new_network_id)
        new_release_date = request.POST['release_date']

        show = Show.objects.get(id=show_id)

        show.title = new_title
        show.description = new_description
        show.network = new_network
        show.release_date = new_release_date
        show.save()

        return redirect(f"/shows/{show.id}")

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('shows')
