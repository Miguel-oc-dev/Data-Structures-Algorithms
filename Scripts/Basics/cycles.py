def cycles():
    # Ciclo For
    for contador in range(0,11):
        print("Contador: ", contador)
    
    name = "Miguel"

    # Recorrido con indices
    for i in range(len(name)):
        caracter = name.lower()[i]
        print(caracter)

    # Recorrido directamente
    for caracter in name:
        print(caracter)

    # For con continue
    for contador in range(1, 11):
        if contador == 6:
            print("Numero ganador", contador)
            continue
        print("Numero: ", contador)

    # While
    num_final = int(input("Ingresa un numero entero: "))
    num_inicial = 1

    while num_inicial <= num_final:
        print(num_inicial)
        num_inicial += 1
    
    while True:
        print("\n---Menú---")
        print("0.- Salir")
        print("1.- Consultar saldo")
        print("2.- Ingresar dinero")
        print("3.- Retirar dinero")
        print("4.- Consultar últimos movimientos")
        print("5.- Convertir divisas")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            print("Tu saldo es de: $1500.00 MXN")
        elif opcion == "2":
            print("Ingrese la cantidad a guardar: ")
        elif opcion == "3":
            print("Retira la cantidad")
        elif opcion == "4":
            print("Último movimiento: Transferencia de $200.00 MXM")
        elif opcion == "5":
            print("Conversión de divisas")
        else:
            print("Opción no válida")


if __name__ == "__main__":
    cycles()