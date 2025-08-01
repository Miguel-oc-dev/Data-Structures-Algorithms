# Nodo de entrada
class Entrada:
    def __init__(self, valor, clave):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashMap:
    def __init__(self, capacidad = 10):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad

    def _hash(self, clave):
        return hash(clave) % self.capacidad
    
    def insertar(self, clave, valor):
        idx = self._hash(clave)
        nodo = self.tabla[idx]

        if nodo is None:
                self.tabla[idx] = Entrada(clave, valor)
                return

        while nodo:
            if nodo.clave == clave:
                nodo.valor = valor
                return
            if nodo.siguiente is None:
                break
            nodo = nodo.siguiente

        nodo.siguiente = Entrada(clave, valor)

    def obtener(self, clave):
        idx = self._hash(clave)
        nodo = self.tabla[idx]
        while nodo:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        return None
    
# Creamos un diccionario
contries = {}

# Creamos las listas de los paises
G = ["Ghana", "Greenland", "Greece"]
I = ["India", "Ireland", "Iran", "Iraq", "Italy"]
U = ["United States", "United Kingdom", "Uruguay"]

# Inicializar el diccionario
contries["G"] = G
contries["I"] = I
contries["U"] = U

# obtener una lista
result = contries.get("I")

if result:
    for contry in result:
        print(contry)


# Eliminar la clave "I"
contries.pop("I", None)

print("Prueba para obtener el valor despues de ser eliminado")
print(contries.get("I"))
print(contries)