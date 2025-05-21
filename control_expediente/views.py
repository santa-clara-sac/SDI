from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CasoJudicialForm
from .models import CasoJudicial, Seguimiento

# @login_required
# def lista_expediente(request):
#     return render(request, 'control_expediente/home.html')

@login_required
def lista_expediente(request):
    form = CasoJudicialForm()

    if request.method == 'POST':
        form = CasoJudicialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control_expediente:lista_expediente')

    caso_judiciales = CasoJudicial.objects.all()

    return render(request, 'control_expediente/home.html', {
        'form': form,
        'caso_judiciales': caso_judiciales,
    })

def editar_expediente(request):
    if request.method == 'POST':
        cj_id = request.POST.get('id')
        cj = get_object_or_404(CasoJudicial, id=cj_id)

        form = CasoJudicialForm(request.POST, instance=cj)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('control_expediente:lista_expediente')
        else:
            print(form.errors)  # Muy útil para debug
            return redirect('control_expediente:lista_expediente')  # o puedes mostrar un error

    return redirect('control_expediente:lista_expediente')

def eliminar_expediente(request, doc_id):
    doc = get_object_or_404(CasoJudicial, id=doc_id)
    doc.delete()
    return redirect('control_expediente:lista_expediente')

#####################################################################################################

from .forms import SeguimientoForm, GastoForm, GastoPresentacionForm, PresentacionForm
from .models import CasoJudicial, Seguimiento, Gasto, Presentacion

# def ver_seguimiento(request, caso_id):
#     caso = get_object_or_404(CasoJudicial, id=caso_id)

#     if request.method == 'POST':
#         if 'seguimiento_id' in request.POST:
#             seguimiento = get_object_or_404(Seguimiento, id=request.POST.get('seguimiento_id'))
#             gasto_form = GastoForm(request.POST, request.FILES)
#             if gasto_form.is_valid():
#                 nuevo_gasto = gasto_form.save(commit=False)
#                 nuevo_gasto.seguimiento = seguimiento
#                 nuevo_gasto.save()
#                 return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)
#             else:
#                 print("Errores del gasto:", gasto_form.errors)
#         else:
#             seguimiento_form = SeguimientoForm(request.POST, request.FILES)
#             if seguimiento_form.is_valid():
#                 nuevo_seguimiento = seguimiento_form.save(commit=False)
#                 nuevo_seguimiento.caso = caso
#                 nuevo_seguimiento.save()
#                 return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)
#             else:
#                 print("Errores del seguimiento:", seguimiento_form.errors)
#     else:
#         seguimiento_form = SeguimientoForm()
#         gasto_form = GastoForm()

#     seguimientos = caso.seguimientos.all().prefetch_related('gastos')

#     context = {
#         'caso': caso,
#         'seguimientos': seguimientos,
#         'form': seguimiento_form,
#         'form2': gasto_form,
#     }
#     return render(request, 'control_expediente/seguimientos_y_gastos.html', context)

from django.db.models import Prefetch

# Prefetch para cargar gastos_presentaciones con sus presentaciones
presentaciones_prefetch = Prefetch('gastos_presentaciones')


def ver_seguimiento(request, caso_id):
    caso = get_object_or_404(CasoJudicial, id=caso_id)

    # Formularios por defecto
    seguimiento_form = SeguimientoForm()
    gasto_form = GastoForm()
    presentacion_form = PresentacionForm()
    gasto_presentacion_form = GastoPresentacionForm()

    if request.method == 'POST':
        tipo_formulario = request.POST.get('tipo_formulario')
        seguimiento_id = request.POST.get('seguimiento_id')

        # Agregar gasto a seguimiento
        if tipo_formulario == 'gasto' and seguimiento_id:
            seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)
            gasto_form = GastoForm(request.POST, request.FILES)
            if gasto_form.is_valid():
                nuevo_gasto = gasto_form.save(commit=False)
                nuevo_gasto.seguimiento = seguimiento
                nuevo_gasto.save()
                return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)

        # Agregar gasto a presentación
        elif tipo_formulario == 'gasto_presentacion' and seguimiento_id:
            presentacion = get_object_or_404(Presentacion, id=seguimiento_id)
            gasto_presentacion_form = GastoPresentacionForm(request.POST, request.FILES)
            if gasto_presentacion_form.is_valid():
                nuevo_gp = gasto_presentacion_form.save(commit=False)
                nuevo_gp.presentacion = presentacion
                nuevo_gp.save()
                return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)

        # Crear nueva presentación
        elif tipo_formulario == 'presentacion':
            presentacion_form = PresentacionForm(request.POST)
            if presentacion_form.is_valid():
                nueva_presentacion = presentacion_form.save(commit=False)
                nueva_presentacion.caso = caso
                nueva_presentacion.save()
                return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)

        # Editar seguimiento existente
        elif tipo_formulario == 'editar_seguimiento' and seguimiento_id:
            seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)
            seguimiento_form = SeguimientoForm(request.POST, request.FILES, instance=seguimiento)
            if seguimiento_form.is_valid():
                seguimiento_editado = seguimiento_form.save(commit=False)
                seguimiento_editado.editor = f"{request.user.first_name} {request.user.last_name}"
                seguimiento_editado.save()
                return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)

        # Crear nuevo seguimiento
        else:
            seguimiento_form = SeguimientoForm(request.POST, request.FILES)
            if seguimiento_form.is_valid():
                nuevo_seguimiento = seguimiento_form.save(commit=False)
                nuevo_seguimiento.caso = caso
                nuevo_seguimiento.usuario = request.user
                nuevo_seguimiento.editor = f"{request.user.first_name} {request.user.last_name}"
                nuevo_seguimiento.save()
                return redirect('control_expediente:ver_seguimiento', caso_id=caso.id)

    # Consultas para mostrar en plantilla
    seguimientos = (
        caso.seguimientos.all()
        .prefetch_related('gastos')
        .order_by('fecha_seguimiento')
    )
    presentaciones = caso.presentaciones.prefetch_related(presentaciones_prefetch)

    # Totales
    total_soles = 0
    total_dolares = 0

    for seguimiento in seguimientos:
        for gasto in seguimiento.gastos.all():
            total_soles += gasto.gastos_soles or 0
            total_dolares += gasto.gastos_dolares or 0

        # Mostrar nombre del creador
        if seguimiento.usuario:
            seguimiento.nombre_usuario = f"{seguimiento.usuario.first_name} {seguimiento.usuario.last_name}"
        else:
            seguimiento.nombre_usuario = "—"

    context = {
        'caso': caso,
        'seguimientos': seguimientos,
        'presentaciones': presentaciones,
        'form': seguimiento_form,
        'form2': gasto_form,
        'form3': presentacion_form,
        'form4': gasto_presentacion_form,
        'total_soles': total_soles,
        'total_dolares': total_dolares,
        'nombre_usuario': f"{request.user.first_name} {request.user.last_name}",
    }

    return render(request, 'control_expediente/seguimientos_y_gastos.html', context)




def editar_seguimiento(request):
    if request.method == 'POST':
        seguimiento_id = request.POST.get('id')
        seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)

        form = SeguimientoForm(request.POST, request.FILES, instance=seguimiento)
        
        if form.is_valid():
            seguimiento_editado = form.save(commit=False)

            # Guardar el nombre del editor actual
            nombre_editor = f"{request.user.first_name} {request.user.last_name}".strip()
            seguimiento_editado.editor = nombre_editor if nombre_editor else request.user.username

            seguimiento_editado.save()
            return redirect('control_expediente:ver_seguimiento', caso_id=seguimiento.caso.id)
        else:
            print("Errores al editar seguimiento:", form.errors)
            return redirect('control_expediente:ver_seguimiento', caso_id=seguimiento.caso.id)

    return redirect('control_expediente:ver_seguimiento', caso_id=0)


def eliminar_seguimiento(request, seguimiento_id):
    seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)
    caso_id = seguimiento.caso.id  # Guardamos antes de eliminar
    seguimiento.delete()
    return redirect('control_expediente:ver_seguimiento', caso_id=caso_id)


def editar_gasto(request):
    if request.method == 'POST':
        gasto_id = request.POST.get('id')
        gasto = get_object_or_404(Gasto, id=gasto_id)

        gasto.fecha = request.POST.get('fecha')
        gasto.detalle = request.POST.get('detalle')
        gasto.codigo_pago = request.POST.get('codigo_pago')
        gasto.gastos_soles = request.POST.get('gastos_soles') or 0
        gasto.gastos_dolares = request.POST.get('gastos_dolares') or 0

        if 'pdf' in request.FILES:
            gasto.pdf = request.FILES['pdf']

        gasto.save()

        return redirect('control_expediente:ver_seguimiento', caso_id=gasto.seguimiento.caso.id)
    

from django.views.decorators.csrf import csrf_protect
@csrf_protect
def eliminar_gasto(request):
    gasto_id = request.POST.get('gasto_id')
    gasto = get_object_or_404(Gasto, id=gasto_id)
    caso_id = gasto.seguimiento.caso.id
    gasto.delete()
    return redirect('control_expediente:ver_seguimiento', caso_id=caso_id)

###############################################################################################

# @login_required
# def listar_gastos_por_seguimiento(request, seguimiento_id):
#     seguimiento = get_object_or_404(Seguimiento, id=seguimiento_id)
#     gastos = seguimiento.gastos.all()  # Usa el related_name='gastos'
    
#     context = {
#         'seguimiento': seguimiento,
#         'gastos': gastos
#     }
#     return render(request, 'control_expediente/listar_gastos.html', context)



def editar_presentacion(request):
    if request.method == 'POST':
        seguimiento_id = request.POST.get('id')
        seguimiento = get_object_or_404(Presentacion, id=seguimiento_id)

        form = PresentacionForm(request.POST, request.FILES, instance=seguimiento)
        
        if form.is_valid():
            form.save()
            return redirect('control_expediente:ver_seguimiento', caso_id=seguimiento.caso.id)
        else:
            print("Errores al editar seguimiento:", form.errors)
            return redirect('control_expediente:ver_seguimiento', caso_id=seguimiento.caso.id)

    return redirect('control_expediente:ver_seguimiento', caso_id=0)


def eliminar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    caso_id = presentacion.caso.id  # Guardamos antes de eliminar
    presentacion.delete()
    return redirect('control_expediente:ver_seguimiento', caso_id=caso_id)