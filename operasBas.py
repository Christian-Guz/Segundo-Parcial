"|-----------------------Operaciones Básicas con Funciones-----------------------|"

import os

def suma():
    while True:
        try:
            os.system("cls")
            a = int(input("Ingrese el número 1: "))
            b = int(input("Ingrese el número 2: "))
            print("\nEl resultado de sumar {} + {} es: {}".format(a,b,a+b))
            input()
            break
        except ValueError:
            print("\nError: Anote un número entero.")
            input()

def resta():
    while True:
        try:
            os.system("cls")
            a = int(input("Ingrese el número 1: "))
            b = int(input("Ingrese el número 2: "))
            print("\nEl resultado de restar {} - {} es: {}".format(a,b,a-b))
            input()
            break
        except ValueError:
            print("\nError: Anote un número entero.")
            input()
    
def multi():
    while True:
        try:
            os.system("cls")
            a = int(input("Ingrese el número 1: "))
            b = int(input("Ingrese el número 2: "))
            print("\nEl resultado de multiplicar {} * {} es: {}".format(a,b,a*b))
            input()
            break
        except ValueError:
            print("\nError: Anote un número entero.")
            input()
    
def divis():
    while True:
        try:
            os.system("cls")
            a = int(input("Ingrese el número 1: "))
            b = int(input("Ingrese el número 2: "))
            if b == 0:
                print("\nError: no puedes dividir entre 0")
                input()
            else:
                print("\nEl resultado de dividir {} / {} es: {}".format(a,b,a/b))
                input()
                break
        except ValueError:
            print("\nError: Anote un número entero.")
            input()
        
def menu():
    opc = 0
    while opc != 5:
        while True:
            try:
                os.system("cls")
                print("Menú\n1.- Suma (+)\n2.- Resta(-)\n3.- Multiplicación (*)\n4.- División (/)\n5.- Salir\n")
                opc = int(input("Selecciona una opción:"))
                if opc == 5:
                    print("\nSaliendo...")
                    break
                else:
                    if opc == 1:
                        suma()
                    elif opc == 2:
                        resta()
                    elif opc == 3:
                        multi()
                    elif opc == 4:
                        divis()
                    else:
                        print("\nError: Anote una opción correcta")
                        input()
                    break
            except ValueError:
                print("\nError: Opción no válida")
                input()

menu()    
    