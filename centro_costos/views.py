from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from django.contrib.auth.hashers import make_password

from .forms import ResponsableForm, ProyectoForm
from .models import Responsable,Proyecto, CentroDeCostos

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
        # Verificamos si se eligió "otros" y se escribió un nuevo centro de costos
        nuevo_centro = request.POST.get('nuevo_centro_de_costos', '').strip()
        if nuevo_centro:
            centro_obj, created = CentroDeCostos.objects.get_or_create(nombre=nuevo_centro)
            request.POST = request.POST.copy()
            request.POST['centro_de_costos'] = centro_obj.id

        form = ProyectoForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_proyectos')

    proyectos = Proyecto.objects.all()
    responsables = Responsable.objects.all()
    centros_de_costos = CentroDeCostos.objects.all()

    return render(request, 'centro_costos/lista_proyectos.html', {
        'form': form,
        'proyectos': proyectos,
        'responsables': responsables,
        'centros_de_costos': centros_de_costos,  # 👈 Agregado aquí
    })

@login_required
def editar_proyecto(request):
    if request.method == 'POST':
        proyecto_id = request.POST.get('id')
        proyecto = get_object_or_404(Proyecto, id=proyecto_id)

        # Creamos el formulario con los datos enviados
        form = ProyectoForm(request.POST, instance=proyecto)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_proyectos')
        else:
            centros_de_costos = CentroDeCostos.objects.all()
            print(form.errors)
            return render(request, 'centro_costos/lista_proyectos.html', {
                'form': form,
                'centros_de_costos': centros_de_costos,
                'errores': form.errors,
            })

    # Si es GET, cargamos el proyecto y los centros disponibles
    proyecto_id = request.GET.get('id')
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    centros_de_costos = CentroDeCostos.objects.all()

    return render(request, 'centro_costos/lista_proyectos.html', {
        'proyecto': proyecto,
        'centros_de_costos': centros_de_costos,
    })

def eliminar_proyecto(request, doc_id):
    doc = get_object_or_404(Proyecto, id=doc_id)
    doc.delete()
    return redirect('centro_costos:lista_proyectos')