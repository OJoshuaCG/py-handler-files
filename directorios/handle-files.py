# Leer archivos
# Opcion 1
archivo = open("archivo.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

# Opcion 2 (modo seguro)
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

# Preferido
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().split("\n")

# Modificar el contenido del archivo (multilinea)
contenido[1] = f"{contenido[1]} escrito desde python!"

# Escribir en un archivo multilinea
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(contenido))

# Escribir mas contenido en un archivo sin borrar su contenido
with open("archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nNueva linea desde python!")

# Crear un archivo y escribir en el
with open("archivo2.txt", "x") as archivo:
    archivo.write("Hola mundo!")
