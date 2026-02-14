import os
os.system("cls")
alumnos = []
while True:
    try:
        num = int(input("¿Cuántos alumnos quieres ingresar?"))
        break #Si la conversación es exitosa, salimos del bucle
    except ValueError:
        print("Error: Por favor ingresa número entero válido.")

for i in range(num):
    nombre = input("Nombre del alumno: ")
    edad = input("Edad del alumno: ")
    materia = input("Materia del alumno: ")
    calificacion = float(input("Calificación del alumno: "))
    
    alumno = {
        "nombre" : nombre,
        "edad" : edad,
        "materia" : materia,
        "calificacion" : calificacion
    }
    alumnos.append(alumno)
    
#Mostrar la cantidad de alumnos registrados

os.system("cls")
print(f"Se ingresaron {len(alumnos)} alumnos.")

#Calcular el promedio de calificaciones
if alumnos:
    total_calificaciones = sum(alumno["calificacion"] for alumno in alumnos)
    promedio = total_calificaciones / len(alumnos)
    print(f"Promedio de calificaciones: {promedio}")
else:
    print("No se ingresaron calificaciones")
    
#Mostrar la lista completa de alumnos
print("Lista completa de alumnos:")
