"""
Create a function that reverses a string
    For example, the string is "Hi how are you?"
    The output should be "?ouy era woh iH"
"""

def reverseString(string):
    # Se crea una lista vacia donde iremos guardando los caracteres en orden inverso
    new_string = []
    # Bucle for para recorrer el string original desde el ultimo caracter hasta el primero
    for i in range(len(string)-1, -1, -1):
        # En cada iteracion, se agrega el caracter correspondiente al final de la nueva lista
        new_string.append(string[i])
        # Se usa para convertir la lista de caracteres en un string
    return ''.join(new_string)

string = "Hello my name is Jack"
print(reverseString(string))