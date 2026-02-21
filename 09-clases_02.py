import os

class operasBas():
    
    def sumar(self):
        self.res = self.n1 + self.n2
        return self.res
    
    def resta(self):
        self.res = self.n1 - self.n2
        return self.res
    
    def multiplicar(self):
        self.res = self.n1 * self.n2
        return self.res
    
    def dividir(self):
        self.res = self.n1 / self.n2
        return self.res
    
    def pedirNumeros(self):
       self.n1 = int(input("n1: "))
       self.n2 = int(input("n2: "))
       
    def imprimir(self):
        print("El resultado es: ",self.res)

obj = operasBas()

def menu():
    op = 0
    while op != 5:
        os.system("cls")
        print("1.- +\n2.- -\n3.- *\n4.- /\n5.- Salir\n")
        op = int(input("Opción: "))
        if op == 1:
            obj.pedirNumeros()
            obj.sumar()
            obj.imprimir()
            input()
        if op == 2:
            obj.pedirNumeros()
            obj.resta()
            obj.imprimir()
            input()
        if op == 3:
            obj.pedirNumeros()
            obj.multiplicar()
            obj.imprimir()
            input()
        if op == 4:
            obj.pedirNumeros()
            obj.dividir()
            obj.imprimir()
            input()
        if op == 5:
            print("Saliendo... ")
        
menu()