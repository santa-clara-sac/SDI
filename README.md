# Proyecto SDI

## Despliegue en desarrollo

### Cambiar la política de ejecución temporalmente

```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
django-admin startproject principal .
python manage.py startapp partidas_planos
python manage.py startapp centro_costos
python manage.py startapp control_expediente
python manage.py startapp hoja_requerimiento
```

## Migraciones

```sh
python manage.py makemigrations
python manage.py migrate partidas_planos
python manage.py createsuperuser
```

## Aditional

#### COLOR PRINCIPAL

```sh
find . -type f \( -name "*.css" -o -name "*.html" -o -name "*.js" \) -exec sed -i 's/#5e81ac/#4c566a/g' {} +
```

#### ADD PATH PARTIDAS

```sh
sed -E "s/(['])([^']+\.pdf)(['])/\1documentos\/partidas\/\2\3/" con_pdf.sql > con_pdf_modificado.sql
```

[https://blog.nonstopio.com/deploy-django-application-on-windows-iis-server-93aee2864c41](https://blog.nonstopio.com/deploy-django-application-on-windows-iis-server-93aee2864c41)

# PATH

```
C:\Users\Admin\Desktop\SDI\.venv\Scripts\python.exe
C:\Users\Admin\Desktop\SDI\.venv\Scripts\wfastcgi.exe

python C:\Users\Admin\Desktop\SDI\.venv\Lib\site-packages\wfastcgi.py
```

C:\inetpub\wwwroot\SDI\.venv\Scripts\python.exe, C:\inetpub\wwwroot\SDI\.venv\Lib\site-packages\wfastcgi.py
