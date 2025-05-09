# Proyecto SDI
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


```sh
find . -type f \( -name "*.css" -o -name "*.html" -o -name "*.js" \) -exec sed -i 's/#02737e/#3b4252/g' {} +
```

#### ADD PATH PARTIDAS

```sh
sed -E "s/(['])([^']+\.pdf)(['])/\1documentos\/partidas\/\2\3/" con_pdf.sql > con_pdf_modificado.sql
```

### Eliminar DB

```sql
ALTER DATABASE SDI_dev SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE SDI_dev;
```

### EXCEL BuscarV

Win + R -> shell:startup

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

- Debe -> ingresa
- Haber -> sale
Saldo = D - H
{% if request.user.role == 3 %}#bf616a{% elif request.user.role == 2 %}#5e81ac{% else %}#3b4252{% endif %}; border: none;

---------------------------------------------------------------------------------------------------------------------------------

N°: Número correlativo del registro en la tabla. Es un identificador secuencial, en este caso es el número 83.
Expediente: Código único que identifica el proceso judicial. Incluye información como el año, número de expediente, tipo de juzgado, y otras referencias internas del sistema judicial.
Sede: Ubicación geográfica o jurisdicción del juzgado que lleva el caso
Especialidad: Categoría jurídica a la que corresponde el caso dentro del sistema judicial.
Materia: Tipo específico de asunto dentro de la especialidad jurídica. En este caso aparece como ODSD, que puede ser un código interno (por ejemplo, Obligaciones Derivadas de Servicios Domiciliarios, si fuese el caso, pero depende del sistema judicial correspondiente).
Juzgado: Nombre y dirección del juzgado que tramita el expediente.
Demandante: Persona o entidad que inician la demanda judicial.
Demandado: Persona o entidad contra quienes se interpone la demanda.
AñoInicio: Año en que se inició el proceso judicial.
