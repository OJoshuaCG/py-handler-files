from pathlib import Path
from os import listdir, scandir, path, walk

raiz = "./"

# Listar todos los ficheros
for fichero in listdir(raiz):
    print(fichero)

# Obtener archivos y carpetas por separados
for fichero in scandir(raiz):
    if fichero.is_dir():
        print("Carpeta: ", fichero.name)
    elif fichero.is_file():
        print("Archivo: ", fichero.name)

# Obtener extension de los archivos
for fichero in scandir(raiz):
    if fichero.is_file():
        directorio, extension = path.splitext(fichero)
        print(f"Archivo: {directorio} --> Extension: {extension}")

# Obtener ruta, carpetas y archivos
ruta, carpetas, ficheros = next(walk(raiz))
print("Ruta:    ", ruta)
print("Carpeta: ", carpetas)
print("Fichero: ", ficheros)
print()

# Obtener raiz, carpeta, archivo de forma recursiva
# for directorio, carpeta, fichero in walk(raiz):
#     print("Raiz:    ", directorio)
#     print("Carpeta: ", carpeta)
#     print("Fichero: ", fichero)
#     print()


# ========== Usando la libreria Path ==========

raiz = Path(".")

# Listar todos los ficheros
for fichero in raiz.iterdir():
    print(fichero)

# Obtener archivos y carpetas por separados
for fichero in raiz.iterdir():
    if fichero.is_dir():
        print("Carpeta : ", fichero)
    elif fichero.is_file():
        print("Archivo : ", fichero)

# # Obtener ruta de los archivos
for fichero in raiz.iterdir():
    if fichero.is_file():
        print("Ruta:  ", fichero.parent)
        print("Archivo:     ", fichero.name)
        print("Extension:   ", fichero.suffix)
        print("Extensiones: ", fichero.suffixes)  # ''.join(fichero.suffixes))
        print()
