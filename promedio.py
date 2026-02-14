import os

os.system("cls")

print("|-----------------------Calculo de promedios-----------------------|")

suma = 0

lista = []

num = int(input("\nIngrese el número de alumnos que quiera registrar: "))

for i in range(num):
    os.system("cls")
    print("Alumno {}".format(i + 1))
    nombre = input("\nIngrese el nombre del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    materia = input("Ingrese la materia del alumno: ")
    calif = float(input("Ingrese la calificación del alumno: "))
    
    alumno = {
        "nombre" : nombre,
        "edad" : edad,
        "materia" : materia,
        "calif" : calif
    }
    
    lista.append(alumno)
    
    #Promedio
    suma = suma + calif 
    
    input("Alumno ingresado...")

prom = suma / num
    
os.system("cls")

i= 0

for x in lista:
    print("\nAlumno {}".format(i + 1))    
    print("Nombre: ",x["nombre"])
    print("Edad: ",x["edad"])
    print("Materia: ",x["materia"])
    print("Calificación: ",x["calif"])
    i += 1
    
print(f"\nEl número de alumnos registrados son: {num}")
print(f"\nEl promedio del grupo es: {prom}")

