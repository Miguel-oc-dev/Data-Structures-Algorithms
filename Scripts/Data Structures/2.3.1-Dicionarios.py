# Crear
d = {}
d["clave"] = "valor"

# Acceder
valor = d.get("clave", "valor_por_defecto")

# Verificar existencia
if "clave" in d:
    print("Existe")

# Iterar
for clave, valor in d.items():
    print(clave, valor)

# Eliminar
del d["clave"]

# Longitud
print(len(d))
