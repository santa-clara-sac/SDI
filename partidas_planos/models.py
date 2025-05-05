from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ESTANDAR = 1
    LEGAL = 2
    ADMINISTRADOR = 3

    ROLE_CHOICE = (
        (ESTANDAR, 'Estandar'),
        (LEGAL, 'Legal'),
        (ADMINISTRADOR, 'Administrador'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

###########################################################################################

class Partida(models.Model):
    codigo = models.CharField(max_length=10)
    partida = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    pg = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    costo = models.CharField(max_length=100)
    centro_costos = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='partidas', blank=True, null=True, max_length=255)


class Plano(models.Model):
    partida = models.CharField(max_length=100,blank=True, null=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    pg = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    costo = models.CharField(max_length=100)
    centro_costos = models.CharField(max_length=100,blank=True, null=True)
    pdf = models.FileField(upload_to='planos_y_otros', blank=True, null=True, max_length=255)



