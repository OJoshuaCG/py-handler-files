# pip install pyyaml
# pip install ruamel.yaml
import yaml
from pathlib import Path
from ruamel.yaml import YAML

# Leer archivo con un Loader
with open("archivo.yaml", 'r') as archivo:
    archivo_yaml = yaml.load(archivo, yaml.SafeLoader)

print(archivo_yaml)
print(type(archivo_yaml))

# Leer archivo sin Loader
with open("archivo.yaml", 'r') as archivo:
    archivo_yaml = yaml.safe_load(archivo)

print(archivo_yaml)
print(type(archivo_yaml))

# Con yaml, puedes tener multiples documentos separados por 3 guiones (---)
# Leer un archivo con varios documentos separados por ---
with open("archivo2.yaml", 'r') as archivo:
    archivo_yaml = yaml.safe_load_all(archivo)

    for _ in archivo_yaml:
        print(_)
        print(type(_))


# Escribir un archivo yaml
documento = """
id: 1
nombre: 'Joshua'
edad: 23
"""

with open('archivo3.yaml', 'w') as archivo:
    # yaml.dump(yaml.safe_load(documento), archivo, yaml.Dumper)
    # OR
    yaml.safe_dump(yaml.safe_load(documento), archivo)


# Escribir en un archivo yaml con un diccionario
documento = {
    "id": 7,
    "nombre": "Orlando",
    "apellido": "Carrasco"
}

with open('archivo3.yaml', 'w') as archivo:
    yaml.safe_dump(documento, archivo)


# ========== ruamel.yaml ==========

ryaml = YAML(typ="safe")

# Leer un archivo
with open("archivo.yaml", 'r') as archivo:
    archivo_yaml = ryaml.load(archivo)

print(archivo_yaml)
print(type(archivo_yaml))

# Leer un archivo con varios documentos separados por ---
with open("archivo2.yaml", 'r') as archivo:
    archivo_yaml = ryaml.load_all(archivo)

    for _ in archivo_yaml:
        print(_)
        print(type(_))

# Escribir un archivo yaml
# Inicializamos el objeto nuevamente (para escribir con string)
ryaml.__init__()
documento = """
id: 1
nombre: 'Joshua'
edad: 23
"""

with open("archivo3.yaml", 'w') as archivo:
    ryaml.dump(ryaml.load(documento), archivo)
print("escritura 1")

# OR
archivo = Path("./archivo3.yaml")
ryaml.dump(ryaml.load(documento), archivo)
print("escritura 2")

# Escribir en un archivo yaml con un diccionario
# ryaml.__init__(typ='safe') # Opcional, se puede usar el parametro typ='safe'
documento = {
    "id": 7,
    "nombre": "Orlando",
    "apellido": "Carrasco"
}
archivo = Path("./archivo3.yaml")

ryaml.dump(documento, archivo)
print("escritura 3")
