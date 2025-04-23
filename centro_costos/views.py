from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.functions import Substr

from .forms import ActividadForm, GastoForm, CantaCallaoForm
from .models import CentroDeCostos, TipoDeGasto, Actividad, Gasto, CantaCallao

def centro_costos_home(request):
     return render(request, 'centro_costos/home.html')

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
        # Verificamos si se eligió "otros" y se escribió un nuevo tipo de gasto
        nuevo_tipo = request.POST.get('nuevo_tipo_gasto', '').strip()
        if nuevo_tipo:
            tipo_obj, created = TipoDeGasto.objects.get_or_create(nombre=nuevo_tipo)
            request.POST = request.POST.copy()
            request.POST['tipo_gasto'] = tipo_obj.id

        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_gastos')

    gastos = Gasto.objects.all().order_by('fecha')
    tipos_de_gasto = TipoDeGasto.objects.all()
    actividades = Actividad.objects.all()

    return render(request, 'centro_costos/lista_gastos.html', {
        'form': form,
        'gastos': gastos,
        'tipos_de_gasto': tipos_de_gasto,
        'actividades': actividades,
    })

@login_required
def editar_gasto(request):
    if request.method == 'POST':
        gasto_id = request.POST.get('id')
        gasto = get_object_or_404(Gasto, id=gasto_id)

        form = GastoForm(request.POST, instance=gasto)

        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_gastos')
        else:
            tipos_de_gasto = TipoDeGasto.objects.all()
            print(tipos_de_gasto)
            print(form.errors)
            return render(request, 'centro_costos/lista_gastos.html', {
                'form': form,
                'tipos_de_gasto': tipos_de_gasto,  # Asegúrate de que este esté presente en el contexto
                'errores': form.errors,
            })

    # Si es GET
    gasto_id = request.GET.get('id')
    gasto = get_object_or_404(Gasto, id=gasto_id)
    tipos_de_gasto = TipoDeGasto.objects.all()
    return render(request, 'centro_costos/lista_gastos.html', {
        'gasto': gasto,
        'tipos_de_gasto': tipos_de_gasto,  # También aquí debes pasar los tipos de gasto
    })

def eliminar_gasto(request, doc_id):
    doc = get_object_or_404(Gasto, id=doc_id)
    doc.delete()
    return redirect('centro_costos:lista_gastos')

#############################################################################

@login_required
def lista_canta_callao(request):
    form = CantaCallaoForm()

    if request.method == 'POST':
        form = CantaCallaoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_canta_callao')

    canta_callao = CantaCallao.objects.annotate(
        anio=Substr('codigo', 8, 2),       # Año: caracteres 8 y 9 (por ejemplo, '19')
        idinterno=Substr('codigo', 4, 3),  # ID interno: caracteres 4-6 (por ejemplo, '001')
    ).order_by('anio', 'idinterno')
    return render(request, 'centro_costos/lista_canta_callao.html', {
        'form': form,
        'canta_callao': canta_callao,
    })

@login_required
def editar_canta_callao(request):
    if request.method == 'POST':
        canta_callao_id = request.POST.get('id')
        canta_callao = get_object_or_404(CantaCallao, id=canta_callao_id)

        form = CantaCallaoForm(request.POST, instance=canta_callao)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centro_costos:lista_canta_callao')
        else:
            print(form.errors)
            return redirect('centro_costos:lista_canta_callao')

    return redirect('centro_costos:lista_canta_callao')

def eliminar_canta_callao(request, doc_id):
    doc = get_object_or_404(CantaCallao, id=doc_id)
    doc.delete()
    return redirect('centro_costos:lista_canta_callao')