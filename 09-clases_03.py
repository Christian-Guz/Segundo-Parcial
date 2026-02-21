import os

class figura:

    def cuadrado(self):
        os.system("cls")
        print("Cuadrado")
        self.l = float(input("\nIngrese el valor de uno de los lados: "))
        self.area = self.l ** 2
        return self.area
    
    def rectangulo(self):
        os.system("cls")
        print("Rectángulo")
        self.b = float(input("\nIngrese el valor de la base: "))
        self.h = float(input("Ingrese el valor de la altura: "))
        self.area = self.b * self.h
        return self.area
    
    def triangulo(self):
        os.system("cls")
        print("Triángulo")
        self.b = float(input("\nIngrese el valor de la base: "))
        self.h = float(input("Ingrese el valor de la altura: "))
        self.area = (self.b * self.h) / 2
        return self.area
    
    def circulo(self):
        os.system("cls")
        print("Círculo")
        self.r = float(input("\nIngrese el valor del radio: "))
        self.area = 3.1416 * (self.r ** 2)
        return self.area
    
    def trapecio(self):
        os.system("cls")
        print("Trapecio")
        self.bM = float(input("\nIngrese el valor de la base mayor: "))
        self.bm = float(input("Ingrese el valor de la base menor: "))
        self.h = float(input("Ingrese el valor de la altura: "))
        self.area = ((self.bM + self.bm) * self.h) / 2
        return self.area
    
    def impresion(self):
        print("\nEl área de la figura es: ",self.area)
        input()
        
def menu():
    fig = figura()
    opc = 0
    while opc != 6:
        os.system("cls")
        print("|-------------------Áreas de Figuras con Clases----------------------|")
        print("\n1.- Cuadrado\n2.- Rectángulo\n3.- Triángulo\n4.- Círculo\n5.- Trapecio\n6.- Salir")
        opc = int(input("Elije una opción: "))
        if opc == 6:
            print("\nSaliendo...")
        else:
            if opc == 1:
                fig.cuadrado()
                fig.impresion()
            elif opc == 2:
                fig.rectangulo()
                fig.impresion()
            elif opc == 3:
                fig.triangulo()
                fig.impresion()
            elif opc == 4:
                fig.circulo()
                fig.impresion()
            elif opc == 5:
                fig.trapecio()
                fig.impresion()
            else:
                print("Error: Anote una opción válida...")
                input()
                
menu()