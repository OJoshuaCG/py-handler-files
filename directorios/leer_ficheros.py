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
        print(f"Archivo: {directorio} === Extension: {extension}")

# # Obtener raiz, carpetas y archivos
directorio, carpetas, ficheros = next(walk(raiz))
print("Raiz:    ", directorio)
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

# for fichero in scandir(raiz):
#     if fichero.is_file():
#         extension = path.splitext(fichero)[1]
#         print(extension)
