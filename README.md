```sh
django-admin startproject principal .
python manage.py startapp partidas_planos
python manage.py startapp centro_costos
python manage.py startapp control_expediente
python manage.py startapp hoja_requerimiento
```

## Migraciones

```sh
python manage.py makemigrations partidas_planos
python manage.py migrate
python manage.py createsuperuser
```

ADD

```sh
find . -type f \( -name "*.css" -o -name "*.html" -o -name "*.js" \) -exec sed -i 's/#5e81ac/#4c566a/g' {} +
```
