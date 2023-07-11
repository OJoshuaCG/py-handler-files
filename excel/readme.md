## Libreria openpyxl

```
pip install openpyxl
```

---
## Crear un excel o cargar un excel

```python
from openpyxl import Workbook, load_workbook

workbook = Workbook()
workbook.save(filename="archivo.xlsx")
workbook.close()

workbook = load_wookbook("archivo.xlsx")
workbook.close()
```


---
## Manipulando hojas de excel

| Codigo                                     | Accion                                       |
| ------------------------------------------ | -------------------------------------------- |
| `workbook.sheetnames`                      | Obtener nombre de hojas                      |
| `workbook.active`                          | Seleccionar hoja activa                      |
| `workbook["nombre_hoja"]`                  | Seleccionar hoja en especifico               |
| `workbook.create_sheet("nombre_hoja")`     | Copiar hoja (objeto hoja)                    |
| `workbook.copy_worksheet(sheet)`           | Copiar hoja (objeto hoja)                    |
| `workbook.remove(sheet)`                   | Eliminar hoja (objeto hoja)                  |
| `sheet.title`                              | Obtener nombre de la hoja                    |
| `sheet.create_sheet("nombre_hoja", index)` | Crear una hoja                               |
| `sheet.sheet_state`                        | Cambiar estado de a `'hidden'` o `'visible'` |
| `sheet.max_row`                            | Cantidad de filas                            |
| `sheet.max_column`                         | Cantidad de columnas                         |
| `sheet.dimension`                          | Rango de celdas ocupadas                     |
| `sheet.calculate_dimension()`              | Rango de celdas ocupadas                     |
| `sheet.sheet_properties`                   | Obtener propiedadades de la hoja             |
| `sheet.sheet_view`                         | Obtener propiedades de vista de la hoja      |
| `sheet.sheet_format`                       | Obtener propiedades del formato de la hoja   |
| `sheet.auto_filter.ref = "X#:X#"`          | Agregar filtro a un rango de celdas          |
| `sheet.freeze_panes = "X#"`                | Bloquear la vista en una fila y/o columna    |


---
## Manipulando celdas

```python
cell = sheet.cell(row, column)
cell = sheet.cell(row, column).value

# Se obtiene unicamente las referencias
# Iterar y obtener sus valores con .value
cell = sheet['A1']
col  = sheet["A"]         # Columna A
cols = sheet["A:B"]       # Columna A -> B
row  = sheet["2"]         # Fila 2
rows = sheet["2:3"]       # Fila 2 -> 3
data = sheet["A1:C2"]     # Rango A1 -> C2
data = sheet["A1":"C2"]   # Rango A1 -> C2

sheet.rows
sheet.columns
sheet.iter_rows(min_row, max_row, min_col, max_col, values_only)
sheet.iter_cols(min_row, max_row, min_col, max_col, values_only)

sheet.append(tuple)

# Insertar filas vacias: indice y cantidad
# Recorre las filas a partir del indice, no sobreescribe los datos
sheet.insert_rows(idx, amount)

# Insertar columnas vacias, indice y cantidad
# Recorre las columnas a partir del indice, no sobreescribe los datosm
sheet.insert_cols(idx, amount)

# Elimina el indice de fila, y la cantidad de filas contando de abajo hacia arriba
# Las filas debajo se recorren hacia arriba
sheet.delete_rows(idx, amount)

# Elimina el indice de columna, y la cantidad de columnas contando de izquierda a derecha
# Las columnas de la derecha, se recorren a la izquierda
sheet.delete_cols(idx, amount)
```

---
## Añadiendo estilos

```python
from openpyxl.styles import Font, Color, Alignment, Border, Side, PatternFill, NamedStyle
# from openpyxl.styles.differential import DifferentialStyle
# from openpyxl.formatting.rule import Rule

sheet['A1'].font = Font(
  size=16
  bold=True,
  italic=False,
  underline='single', # {'single', 'double', 'doubleAccounting', 'singleAccounting'}
  color="00FF0000")

sheet['A1'].alignment = Alignment(
  horizontal="center",
  vertical="top")

# boder_style = {'dotted', 'thick', 'mediumDashed', 'medium', 'slantDashDot', 'mediumDashDotDot', 'mediumDashDot', 'dashDot', 'hair', 'double', 'thin', 'dashDotDot', 'dashed'}
double_border_side = Side(border_style="double")

sheet['A1'].border = Border(
  top=Side(border_style="medium"),
  right=double_border_side,
  bottom=double_border_side,
  left=double_border_side)

sheet['A1'].fill = PatternFill('solid', start_color="38e3ff")


# Creando un template
template = NamedStyle(name="header")
template.font = Font(bold=True)
template.border = Border(bottom=Side(border_style="thin"))
template.alignment = Alignment(horizontal="center", vertical="center")
```

---
## Estilos condicionales

Agregando un estilo condicional, donde:
- Si el valor de la columna `H` es menor a 3, se rellenara de rojo la fila

```python
from openpyxl.styles import PatternFill
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule

# Creando el color a rellenar
red_background = PatternFill(fgColor="00FF0000")
# Creando el objeto que tendra los estilos que seran diferenciadores
# En este mismo, se pueden añadir mas estilos
diff_style = DifferentialStyle(fill=red_background)

# Se crea la regla
rule = Rule(type="expression", dxf=diff_style)
rule.formula = ["$H1<3"]

# Se agrega la regla a un rango de celdas
sheet.conditional_formatting.add("A1:O100", rule)
workbook.save("sample_conditional_formatting.xlsx")
```

Las reglas nos permiten crear 3 formatos diferentes.

- **ColorScale**. Recibe un valor minimo, el color para ese valor minimo, un valor maximo y el color del valor maximo.

```python
 from openpyxl.formatting.rule import ColorScaleRule

 # Se crea un
 color_scale_rule = ColorScaleRule(
  start_type="min",
  start_color="00FF0000",  # Red
  end_type="max",
  end_color="0000FF00")  # Green

 # Se agrega la regla a un rango de celdas
 sheet.conditional_formatting.add("H2:H100", color_scale_rule)
 workbook.save(filename="sample_conditional_formatting_color_scale.xlsx")

 # Otro ejemplo de una regla de escala
color_scale_rule = ColorScaleRule(
  start_type="num",
  start_value=1,
  start_color="00FF0000",  # Red
  mid_type="num",
  mid_value=3,
  mid_color="00FFFF00",  # Yellow
  end_type="num",
  end_value=5,
  end_color="0000FF00")  # Green
```

- **IconSet**. Se agrega un icono de acuerdo a su valor.

```python
from openpyxl.formatting.rule import IconSetRule

# {‘3Arrows’, ‘3ArrowsGray’, ‘3Flags’, ‘3TrafficLights1’, ‘3TrafficLights2’, ‘3Signs’, ‘3Symbols’, ‘3Symbols2’, ‘4Arrows’, ‘4ArrowsGray’, ‘4RedToBlack’, ‘4Rating’, ‘4TrafficLights’, ‘5Arrows’, ‘5ArrowsGray’, ‘5Rating’, ‘5Quarters’}
icon_set_rule = IconSetRule("5Arrows", "num", [1, 2, 3, 4, 5])

sheet.conditional_formatting.add("H2:H100", icon_set_rule)
workbook.save("sample_conditional_formatting_icon_set.xlsx")

```

---
## Imagenes y graficas


---
## Formulas con excel



---
## Fuentes:

- [https://www.datacamp.com/tutorial/python-excel-tutorial](https://www.datacamp.com/tutorial/python-excel-tutorial)
- [https://www.geeksforgeeks.org/working-with-excel-spreadsheets-in-python/](https://www.geeksforgeeks.org/working-with-excel-spreadsheets-in-python/)
- [https://realpython.com/openpyxl-excel-spreadsheets-python/](https://realpython.com/openpyxl-excel-spreadsheets-python/)
- [https://pybonacci.org/2021/03/10/curso-sobre-como-trabajar-con-hojas-de-calculo-excel-calc-usando-openpyxl-en-python-iii/](https://pybonacci.org/2021/03/10/curso-sobre-como-trabajar-con-hojas-de-calculo-excel-calc-usando-openpyxl-en-python-iii/)
- [https://openpyxl.readthedocs.io/en/stable/formatting.html#iconset](https://openpyxl.readthedocs.io/en/stable/formatting.html#iconset)
