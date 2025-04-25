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
```

## Migraciones

```sh
python manage.py makemigrations partidas_planos
python manage.py migrate partidas_planos
python manage.py makemigrations centro_costos
python manage.py migrate centro_costos
python manage.py migrate
```

## Aditional

#### COLOR PRINCIPAL
##### POLAR NIGHT
#2e3440
#3b4252
#434c5e
#4c566a
###### SNOW STORM
#d8dee9
#e5e9f0
#eceff4
##### FROST
#8fbcbb
#88c0d0
#81a1c1
#5e81ac
##### AURORA
#bf616a
#d08770
#ebcb8b
#a3be8c
#b48ead

```sh
find . -type f \( -name "*.css" -o -name "*.html" -o -name "*.js" \) -exec sed -i 's/#02737e/#3b4252/g' {} +
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

### Eliminar DB

```sql
ALTER DATABASE SDI_dev SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE SDI_dev;
```

### EXCEL BuscarV

```
=SI.ERROR(BUSCARV(A4,Table1[#Todo], 9, FALSO), "")
```

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\Admin\Desktop\SDI\iniciar_server.bat" & Chr(34), 0
Set WshShell = Nothing

Msg 2627, Level 14, State 1, Line 1861
Violation of UNIQUE KEY constraint 'UQ__centro_c__40F9A206D69EA8F9'. Cannot insert duplicate key in object 'dbo.centro_costos_cantacallao'. The duplicate key value is (CC-019-22).

INSERT INTO [centro_costos_cantacallao] (codigo, fecha, concepto, detalle, referencia, monto1, monto2) VALUES ('CC-019-22', '2022-06-11', 'Gastos Canta Callao', 'PINTADO DEL TEJADO Y PARTE DEL TECHO, FACHADA', '', '1356.6', '');
INSERT INTO [centro_costos_cantacallao] (codigo, fecha, concepto, detalle, referencia, monto1, monto2) VALUES ('CC-019-22', '2022-02-16', 'Municipalidad de los Olivos', '1 SOLICITUD DE CERTIFICACION DE NUMERACION A-1-4', '', '44', '');

- Codigo (identificacion del documento XX-XXX-XX -> CentroCosto-Sello-Año)
- Fecha (fecha en la q se realizó el gasto)
- Detalle (descripcion del gasto)
- Referencia (codigo del gasto bancario/boleta/)
- PDF (archivo de sustento)
- Monto Soles (monto del gasto)
- Monto Dolares (monto del gasto)
- Actividad (proyecto, obra, servicio o actividad específica donde se realizó el gasto [PinturaFachada, CajaDeLuzEnel, ReparacionDeTecho])
- Tipo Gasto (Representa para qué fin contable se usó el dinero [ManoDeObra, Materiales, etc])