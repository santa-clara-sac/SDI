from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login as auth_login

from .forms import PartidaForm,PlanoForm
from .models import Partida,Plano, User

@login_required
def documentacion(request):
    return render(request, 'partidas_planos/home.html')

@login_required
def lista_partidas(request):
    # if request.user.role != User.ADMINISTRADOR:
    #     return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    form = PartidaForm()

    if request.method == 'POST':
        form = PartidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_partidas')  # O el nombre de tu vista actual

    partidas = Partida.objects.all()  # Si quieres listarlas en la plantilla

    return render(request, 'partidas_planos/lista_partidas.html', {
        'form': form,
        'partidas': partidas,
    })


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Cambia según el nombre de tu vista home
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})

    return render(request, 'login.html')

def editar_partida(request):
    if request.method == 'POST':
        partida_id = request.POST.get('id')
        partida = get_object_or_404(Partida, id=partida_id)

        form = PartidaForm(request.POST, request.FILES, instance=partida)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('lista_partidas')
        else:
            print(form.errors)  # Muy útil para debug
            return redirect('lista_partidas')  # o puedes mostrar un error

    return redirect('lista_partidas')

def eliminar_partida(request, doc_id):
    doc = get_object_or_404(Partida, id=doc_id)
    doc.delete()
    return redirect('lista_partidas')


##########################################################################

@login_required
def lista_planos(request):
    # if request.user.role != User.ADMINISTRADOR:
    #     return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    form = PlanoForm()

    if request.method == 'POST':
        form = PlanoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_planos')

    planos = Plano.objects.all()

    return render(request, 'partidas_planos/lista_planos.html', {
        'form': form,
        'planos': planos,
    })

@login_required
def editar_plano(request):
    if request.method == 'POST':
        plano_id = request.POST.get('id')
        plano = get_object_or_404(Plano, id=plano_id)

        form = PlanoForm(request.POST, request.FILES, instance=plano)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('lista_planos')
        else:
            print(form.errors)
            return redirect('lista_planos')

    return redirect('lista_planos')

@login_required
def eliminar_plano(request, doc_id):
    plano = get_object_or_404(Plano, id=doc_id)
    plano.delete()
    return redirect('lista_planos')
