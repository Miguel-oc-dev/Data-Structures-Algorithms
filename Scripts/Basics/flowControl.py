def main():
    # if
    if 15 > 20:
        print("15 es menor que 20")
    
    # if-else
    nombre = input("Ingresa tu nombre: ")
    edad = int(input(f"{nombre}, ingresa tu edad: "))

    if edad >= 18:
        print(f"{nombre}, eres mayor de edad.")
    else:
        print(f"{nombre}, eres menor de edad")

    """
        Determina si una persona es un bebé (0-2 años), un niño (3-11 años),
        un adolescente (12-17 años) y un adulto joven (18-59 años) o mayor (60 o más)
    """
    age = int(input(f"{nombre}, ingresa tu edad: "))

    if age >= 18:
        if age < 60:
            print("Eres un adulto joven")
        else:
            print("Eres un adulto mayor")
    elif(age >= 12):
        print("Eres un adolescente")
    elif(age >= 3):
        print("Eres un niño")
    else:
        print("Eres un bebé")


    # Determina si una variable (String) contiene texto o esta vacio
    texto = "CH56"

    if texto == "":
        print("vacio")
    else:
        print(f"Tu texto es: {texto}")

    # Operador ternario 
    estado = "No hay nada" if texto == "" else "Tiene texto"
    print(estado)

if __name__ == "__main__":
    main()
