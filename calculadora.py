while True:
    print("|1| SUMAR")
    print("|2| RESTAR")
    print("|3| MULTIPLICAR")
    print("|4| DIVIDIR")
    print("|5| APAGAR CALCULADORA")
    opc=int(input("ingrese una opcion:"))
    if opc <=0:
        print(" |!ERROR¡| Recuerda que las opciones son del (1-5)\n"
        "Escoge una opcion")
    elif opc == 1:
        def sumarNumero(a,b):
            return a+b
        a=int(input("ingrese un numero:"))
        b=int(input("ingrese un numero:"))
        print(f"la suma de los numero es {sumarNumero}")
            
