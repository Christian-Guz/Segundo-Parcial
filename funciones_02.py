import os

def suma():
    os.system("cls")
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    res = a + b
    return res
    input()
    
def resta():
    os.system("cls")
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    res = a - b
    print("La resta es: ",res)
    input()
    
def menu():
    op = 0
    while op != 5:
        os.system("cls")
        print("1.- + \n2.- -\n3.- *\n4.- /\n5.- Salir\n")
        op = int(input("OPCION: "))
        if op == 1:
            suma()
        if op == 2:
            resta()

if __name__==("__main__"):
    menu()
        
    