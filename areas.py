import os

os.system("cls")

def cuadrado():
    while True:
        try:
            os.system("cls")
            print("Cuadrado:")
            l = float(input("\nIngrese el valor de uno de sus lados: "))
            area = l ** 2
            print("\nEl área del cuadrado es: ",area)
            input()
            break
        except ValueError:
            print("Error: Anote un valor numérico...")
            input()

def rectangulo():
    while True:
        try:
            os.system("cls")
            print("Rectángulo:")
            b = int(input("\nIngrese el valor de la base: "))
            h = int(input("Ingrese el valor de la altura: "))
            area = b * h
            print("\nEl área del rectángulo es de: ",area)
            input()
            break
        except ValueError:
            print("Error: Anote un valor numérico...")
            input()

def triangulo():
    while True:
        try:
            os.system("cls")
            print("Triángulo:")
            b = float(input("\nIngrese el valor de la base: "))
            h = float(input("Ingrese el valor de la altura: "))
            area = (b * h) / 2
            print("\nEl área del triángulo es de: ",area)
            input()
            break
        except ValueError:
            print("Error: Anote un valor numérico...")
            input()

def circulo():
    while True:
        try:
            os.system("cls")
            print("Círculo:")
            r = float(input("\nIngrese el valor del radio: "))
            area = 3.1416 * (r**2)
            print("\nEl área del círculo es de: ",area)
            input()
            break
        except ValueError:
            print("Error: Anote un valor numérico...")
            input()

def trapecio():
    while True:
        try:
            os.system("cls")
            print("Trapecio:")
            bM = float(input("\nIngrese el valor de la base mayor: "))
            bm = float(input("Ingrese el valor de la base menor: "))
            h = float(input("Ingrese el valor de la alutra: "))
            area = ((bm + bM) * h) / 2
            print("\nEl área del trapecio es de: ",area)
            input()
            break
        except ValueError:
            print("Error: Anote un valor numérico...")
            input()
            
def menu():
    while True:
        try:
            opc = 0
            while opc != 6:
                os.system("cls")
                print("|-------------------------Calculo de áreas-----------------------|")
                print("\nMENU\n1.- Cuadrado\n2.- Rectángulo\n3.- Triángulo\n4.- Círculo\n5.- Trapecio\n6.- Salir")
                opc = int(input("\nElija una opción: "))
                if opc == 6:
                    print("\nSaliendo...")
                else:
                    if opc == 1:
                        cuadrado()
                    elif opc == 2:
                        rectangulo()
                    elif opc == 3:
                        triangulo()
                    elif opc == 4:
                        circulo()
                    elif opc == 5:
                        trapecio()
                    else:
                        print("\nError: Elija un opción válida...")
                        input()
            break
        except ValueError:
            print("\nError: Elija una opción numércia válida...")
            input()
            
menu()