"Un diccionario es una estructura de datos que almacena infromación en pares clave-valor"

"No se accede por posición, si no por clave"

"""
Ejemplo:

alumno = {
    "nombre" : "Ana",
    "edad" : 21,
    "carrera" : "Ingeniería"}
    
"""

alumno = {
    "nombre" : "Ana",
    "edad" : 21,
    "carrera" : "Ingeniería"
}
print(type(alumno))
print(alumno)
print("print(alumno['nombre']) = ",alumno["nombre"])
print("print(alumno.get('edad') = ",alumno.get("edad"))

alumno["promedio"] = 9.2
print (alumno)
alumno["edad"] = 22
print(alumno)

del alumno["carrera"]
print(alumno)

for clave in alumno:
    print(clave)
    print(clave, ":", alumno[clave])
    
print("Cantidad de pares clave-valor: ",len(alumno))
print("Claves del diccionario: ",alumno.keys())
print("Valores del diccionarios: ",alumno.values())
print("Pares clave-valor: ",alumno.items())

alumno1 = {
    "nombre" : "",
    "edad" : 0,
    "carrera" : ""
}

ico201 =[alumno1,alumno1,alumno1]