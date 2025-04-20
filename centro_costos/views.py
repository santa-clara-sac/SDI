from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from django.contrib.auth.hashers import make_password

from .forms import ResponsableForm, ProyectoForm
from .models import Responsable,Proyecto

def centro_costos_home(request):
    return render(request, 'centro_costos/home.html')

@login_required
def lista_responsables(request):

    form = ResponsableForm()

    if request.method == 'POST':
        form = ResponsableForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_responsables') 

    responsables = Responsable.objects.all()  

    return render(request, 'centro_costos/lista_responsables.html', {
        'form': form,
        'responsables': responsables,
    })


def editar_responsable(request):
    if request.method == 'POST':
        responsable_id = request.POST.get('id')
        responsable = get_object_or_404(Responsable, id=responsable_id)

        form = ResponsableForm(request.POST, instance=responsable)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_responsables')
        else:
            print(form.errors)  # Muy útil para debug
            return redirect('lista_responsales')

    return redirect('lista_responsables')

def eliminar_responsable(request, doc_id):
    doc = get_object_or_404(Responsable, id=doc_id)
    doc.delete()
    return redirect('centro_costos:lista_responsables')

#############################################################################################

@login_required
def lista_proyectos(request):

    form = ProyectoForm()

    if request.method == 'POST':
        form = ProyectoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_proyectos') 

    proyectos = Proyecto.objects.all()
    responsables = Responsable.objects.all()

    return render(request, 'centro_costos/lista_proyectos.html', {
        'form': form,
        'proyectos': proyectos,
        'responsables': responsables,
    })

def editar_proyecto(request):
    if request.method == 'POST':
        proyecto_id = request.POST.get('id')
        proyecto = get_object_or_404(Proyecto, id=proyecto_id)

        # Si el usuario eligió "Otros", reemplazamos el valor antes de pasar al form
        centro_custom  = request.POST.get('nuevo_centro_de_costos')
        if request.POST.get('centro_de_costos') == 'Otros' and centro_custom :
            # Creamos un diccionario mutable con los datos del POST
            post_data = request.POST.copy()
            post_data['centro_de_costos'] = centro_custom 
            form = ProyectoForm(post_data, instance=proyecto)
        else:
            form = ProyectoForm(request.POST, instance=proyecto)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_proyectos')
        else:
            print(form.errors)
            return redirect('centro_costos:lista_proyectos')
    
    # En caso de que desees usar GET para renderizar el formulario de edición
    centros = Proyecto.objects.values_list('centro_de_costos', flat=True).distinct()
    centros = sorted(set(centros))

    return render(request, 'tu_template.html', {
        'centros_de_costos': centros,
    })