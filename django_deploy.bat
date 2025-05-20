@echo off
cd /d C:\Users\User\Desktop\SDI
call .venv\Scripts\activate

:loop
echo Iniciando el servidor Django...
python manage.py runserver 0.0.0.0:9090

REM Si el servidor falla, mostrar una ventana emergente
IF %ERRORLEVEL% NEQ 0 (
    echo El servidor falló. Mostrando mensaje de advertencia...
    mshta "javascript:alert('Error al iniciar el servidor. Se reintentará en 5 segundos.');close();"
    timeout /t 5
    goto loop
)
