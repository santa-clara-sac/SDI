from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from django.contrib.auth.hashers import make_password

from .forms import ActividadForm, GastoForm
from .models import CentroDeCostos, TipoDeGasto, Actividad, Gasto

def centro_costos_home(request):
     return render(request, 'centro_costos/home.html')

# @login_required
# def lista_responsables(request):

#     form = ResponsableForm()

#     if request.method == 'POST':
#         form = ResponsableForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('centro_costos:lista_responsables') 

#     responsables = Responsable.objects.all()  

#     return render(request, 'centro_costos/lista_responsables.html', {
#         'form': form,
#         'responsables': responsables,
#     })


# def editar_responsable(request):
#     if request.method == 'POST':
#         responsable_id = request.POST.get('id')
#         responsable = get_object_or_404(Responsable, id=responsable_id)

#         form = ResponsableForm(request.POST, instance=responsable)
#         # print(form)
#         # print(form.is_valid())
#         if form.is_valid():
#             form.save()
#             return redirect('centro_costos:lista_responsables')
#         else:
#             print(form.errors)  # Muy útil para debug
#             return redirect('lista_responsales')

#     return redirect('lista_responsables')

# def eliminar_responsable(request, doc_id):
#     doc = get_object_or_404(Responsable, id=doc_id)
#     doc.delete()
#     return redirect('centro_costos:lista_responsables')

# #############################################################################################

@login_required
def lista_actividades(request):
    form = ActividadForm()

    if request.method == 'POST':
        # Verificamos si se eligió "otros" y se escribió un nuevo centro de costos
        nuevo_centro = request.POST.get('nuevo_centro_de_costos', '').strip()
        if nuevo_centro:
            centro_obj, created = CentroDeCostos.objects.get_or_create(nombre=nuevo_centro)
            request.POST = request.POST.copy()
            request.POST['centro_de_costos'] = centro_obj.id

        form = ActividadForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_actividades')

    actividades = Actividad.objects.all()
    centros_de_costos = CentroDeCostos.objects.all()

    return render(request, 'centro_costos/lista_actividades.html', {
        'form': form,
        'actividades': actividades,
        'centros_de_costos': centros_de_costos,
    })

@login_required
def editar_actividad(request):
    if request.method == 'POST':
        actividad_id = request.POST.get('id')
        actividad = get_object_or_404(Actividad, id=actividad_id)

        # Creamos el formulario con los datos enviados
        form = ActividadForm(request.POST, instance=actividad)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_actividades')
        else:
            centros_de_costos = CentroDeCostos.objects.all()
            print(form.errors)
            return render(request, 'centro_costos/lista_actividades.html', {
                'form': form,
                'centros_de_costos': centros_de_costos,
                'errores': form.errors,
            })

    # Si es GET, cargamos el proyecto y los centros disponibles
    actividad_id = request.GET.get('id')
    actividad = get_object_or_404(Actividad, id=actividad_id)
    centros_de_costos = CentroDeCostos.objects.all()

    return render(request, 'centro_costos/lista_actividades.html', {
        'actividad': actividad,
        'centros_de_costos': centros_de_costos,
    })

def eliminar_actividad(request, doc_id):
    doc = get_object_or_404(Actividad, id=doc_id)
    doc.delete()
    return redirect('centro_costos:lista_actividades')

#########################################################################################

@login_required
def lista_gastos(request):
    form = GastoForm()

    if request.method == 'POST':
        # Verificamos si se eligió "otros" y se escribió un nuevo centro de costos
        nuevo_centro = request.POST.get('nuevo_centro_de_costos', '').strip()
        if nuevo_centro:
            centro_obj, created = TipoDeGasto.objects.get_or_create(nombre=nuevo_centro)
            request.POST = request.POST.copy()
            request.POST['centro_de_costos'] = centro_obj.id

        form = GastoForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_gastos')

    gastos = Gasto.objects.all()
    centros_de_costos = TipoDeGasto.objects.all()

    return render(request, 'centro_costos/lista_gastos.html', {
        'form': form,
        'gastos': gastos,
        'centros_de_costos': centros_de_costos,
    })