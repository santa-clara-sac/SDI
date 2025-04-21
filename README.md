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
#02737e
find . -type f \( -name "*.css" -o -name "*.html" -o -name "*.js" \) -exec sed -i 's/#434c5e/#02737e/g' {} +
```

#### ADD PATH PARTIDAS

```sh
sed -E "s/(['])([^']+\.pdf)(['])/\1documentos\/partidas\/\2\3/" con_pdf.sql > con_pdf_modificado.sql
```

# IMG BACKGROUND

```css
body {
  background-image: url("{% static 'images/bg.png' %}");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 100vh;
  margin: 0;
  position: relative;
}

body::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(216, 222, 233, 0.495);
  /* Cambia el 0.4 para más o menos claridad */
  z-index: 0;
}
```
