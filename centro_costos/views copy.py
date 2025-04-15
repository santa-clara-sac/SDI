from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from partidas_planos.models import User
from .forms import UserForm, UserEditForm
from django.contrib.auth.hashers import make_password


def centro_costos_home(request):
    return render(request, 'centro_costos/home.html')

