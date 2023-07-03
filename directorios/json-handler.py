import json

# json.load y json.dump usados para archivos
archivo = open("archivo.json", "r")
archivo_json = json.load(archivo)
print(archivo_json)
print(type(archivo_json))
archivo.close()

for key in archivo_json.keys():
    print("key: ", key)


for valor in archivo_json.values():
    print("Valor: ", valor)


for key, valor in archivo_json.items():
    print(f"{key} -> {valor}")


archivo_json["nombre"] = "Orlando"

archivo = open("archivo.json", "w")
json.dump(archivo_json, archivo, indent=4)
archivo.close()


# dumps : convierte un diccionario a un string
# loads : convierte un string a un diccionario
diccionario = {
    "name": "Alice",
    "city": "Madrid"
}

texto = json.dumps(diccionario, indent=4)
# Otros parametros para 'dumps'
# (objeto, indent=4, sort_keys=True, separators=(('. ', ' = ')))
# separators por default: (',', ': ')

diccionario = json.loads(texto)
