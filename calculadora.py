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
        print("|veo que quieres sumar|")
        a=str(input("ingrese un numero:"))
        b=str(input("ingrese un numero:"))
        print(f"la suma de los numero es {sumarNumero}")
    elif opc == 2:
        def restarNumero(a,b):
            return a-b
        print("|veo que quieres restar")
        a=str(input("ingrese un numero"))
        b=str(input("ingrese un numero"))
        print(f"la resta de los numero es {restarNumero}")
        
            
