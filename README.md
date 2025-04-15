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

## IIS
```ps1
Enable-WindowsOptionalFeature -Online -FeatureName IIS-WebServerRole -All
dism /online /enable-feature /featurename:IIS-CGI /all
```

[https://blog.nonstopio.com/deploy-django-application-on-windows-iis-server-93aee2864c41](https://blog.nonstopio.com/deploy-django-application-on-windows-iis-server-93aee2864c41)

# PATH
```
C:\Users\Admin\Desktop\SDI\.venv\Scripts\python.exe
C:\Users\Admin\Desktop\SDI\.venv\Scripts\wfastcgi.exe

python C:\Users\Admin\Desktop\SDI\.venv\Lib\site-packages\wfastcgi.py
```


# Variables
$siteName = "DjangoSDI"
$sitePort = 82
$sitePath = "C:\Users\Admin\Desktop\SDI"
$pythonPath = "$sitePath\.venv\Scripts\python.exe"
$wfastcgiPath = "$sitePath\.venv\Lib\site-packages\wfastcgi.py"
$handlerName = "Python FastCGI"
$binding = "http/*:${sitePort}:"

# Ruta a appcmd
$appcmd = "$env:windir\system32\inetsrv\appcmd.exe"

# 1. Agregar entrada FastCGI si no existe
Write-Host "📦 Agregando configuración de FastCGI..."
& $appcmd set config /section:system.webServer/fastCgi /+"[fullPath='$pythonPath', arguments='$wfastcgiPath']" 2>$null

# 2. Crear nuevo sitio IIS
Write-Host "🌐 Creando sitio '$siteName' en IIS..."
& $appcmd add site /name:$siteName /bindings:$binding /physicalPath:$sitePath

# 3. Configurar handler para Python + FastCGI
Write-Host "🔧 Configurando handler..."
& $appcmd set config $siteName /section:system.webServer/handlers /+"[name='$handlerName', path='*', verb='*', modules='FastCgiModule', scriptProcessor='$pythonPath|$wfastcgiPath', resourceType='Unspecified', requireAccess='Script']"

# 4. Variables de entorno para FastCGI
Write-Host "🧪 Estableciendo variables de entorno..."
& $appcmd set config /section:system.webServer/fastCgi /+"[fullPath='$pythonPath', arguments='$wfastcgiPath'].environmentVariables.[name='WSGI_HANDLER',value='principal.wsgi.application']"
& $appcmd set config /section:system.webServer/fastCgi /+"[fullPath='$pythonPath', arguments='$wfastcgiPath'].environmentVariables.[name='DJANGO_SETTINGS_MODULE',value='principal.settings']"
& $appcmd set config /section:system.webServer/fastCgi /+"[fullPath='$pythonPath', arguments='$wfastcgiPath'].environmentVariables.[name='PYTHONPATH',value='$sitePath']"

# 5. Listo
Write-Host "`n✅ Sitio '$siteName' creado correctamente en http://localhost:$sitePort/"
