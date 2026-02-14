import os

os.system("cls")

print("|--------------------------Captura de Alumnos-----------------------------|")

num = int(input("Ingrese el número de alumnos: "))

lista = []

i = 0

while i < num:
    os.system("cls")
    
    nombre = input("\nAnote el nombre del alumno {}: ".format(i+1))
    edad = input("\nAnote la edad del alumno {}: ".format(i+1))
    carrera = input("\nAnote la carrera del alumno {}: ".format(i+1))
    
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera}
    
    lista.append(alumno)
    
    input("\nAlumno registrado")
    
    i += 1

i = 0    
os.system("cls")   
for x in lista:
    print("\nAlumno {}:".format(i + 1))
    print("Nombre: ",x["nombre"])
    print("Edad: ",x["edad"])
    print("Carrera: ",x["carrera"])
    i +=1
    
