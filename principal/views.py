from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from .forms import UserForm, UserEditForm
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, 'home.html')


@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])  # Hashea la contraseña
            usuario.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect('lista_usuarios')
    else:
        form = UserForm()

    return render(request, 'administrador/home.html', {
        'usuarios': usuarios,
        'form': form,
    })


@login_required
def editar_usuario(request):
    if request.method == 'POST':
        usuario = get_object_or_404(User, id=request.POST.get('id'))
        form = UserEditForm(request.POST, instance=usuario)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Usuario actualizado correctamente.")
        else:
            messages.error(request, "Hubo un error al actualizar el usuario.")

    return redirect('lista_usuarios')

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    return redirect('lista_usuarios')


def cambiar_password_usuario(request):
    if request.method == "POST":
        user_id = request.POST.get("id")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(user_id)
        print(password)
        print(confirm_password)
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('lista_usuarios')

        try:
            user = User.objects.get(id=user_id)
            user.password = make_password(password)  # Hashear la contraseña
            user.save()
            messages.success(request, "Contraseña actualizada correctamente.")
        except User.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    return redirect('lista_usuarios')