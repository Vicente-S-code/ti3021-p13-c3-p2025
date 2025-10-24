def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b  # OJO: si b es 0, dará error (versión básica)

def mostrar_menu():
    print("===| CALCULADORA |===")
    print("1) SUMAR")
    print("2) RESTAR")
    print("3) MULTIPLICAR")
    print("4) DIVIDIR")
    print("5) SALIR")

while True:
    mostrar_menu()
    opc = int(input("Elige una opción (1-5): "))

    if opc == 5:
        print("Saliendo de la calculadora. ¡Chao!")
        break
    elif opc >= 1 and opc <= 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opc == 1:
            resultado = sumar(a, b)
            print("Resultado de la suma:", resultado)
        elif opc == 2:
            resultado = restar(a, b)
            print("Resultado de la resta:", resultado)
        elif opc == 3:
            resultado = multiplicar(a, b)
            print("Resultado de la multiplicación:", resultado)
        elif opc == 4:
            # Versión básica: no maneja división por cero
            resultado = dividir(a, b)
            print("Resultado de la división:", resultado)
    else:
        print("Opción inválida. Recuerda que solo hay opciones del 1 al 5.")
        
            
