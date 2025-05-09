from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CasoJudicialForm
from .models import CasoJudicial

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

def ver_seguimiento(request, caso_id):
    caso = get_object_or_404(CasoJudicial, id=caso_id)
    seguimientos = caso.seguimientos.all().prefetch_related('gastos')

    context = {
        'caso': caso,
        'seguimientos': seguimientos,
    }
    return render(request, 'control_expediente/seguimientos_y_gastos.html', context)