"""
Las funciones en Python son bloques de código reutilizables que realizan una tarea específica.
Sirve para organizar, reutilizar y hacer más claro el código.

Para qué sirve?

* Evitan repetir código
* Permiten dividir un problema grande en partes pequeñas
* Hacen el programa más fácil de mantener
* Mejoran la legibilidad

#En Python se deginen con la palabra clave def:

#Ejemplo:
def nombre_funcion(parametro)
    # bloque de código
    return valor"""
    
def nombre(): #Funcion que no resive nada ni regresa nada
    print("Hola mundo")
    
nombre()

def suma(): #Función que no resive parámetros pero si regresa algo
    a = 6
    print("Dentro de la función: ",a)
    b  = 7 
    #o c = a + b y return c, es lo mismo
    return a + b

a = 3
print("Fuera de la función: ",a)
b = 7
c = a+b

print(suma())

def multiplica(x,y):
    return x*y


print("La multiplicación es: ",multiplica(6,7)) #Si no colocas nada marcará error
print("La multiplicación es: ",multiplica(a,b))

"""
operasBas.py

Realizar
1.- +
2.- -
3.- *
4.- /
5.- Salir

Pedir la opción con un menu(), y cada operación será una función:
suma(), resta(), dividir(), multiplicar()
  --Antes de limpiar pantalla, mostrar resultado de la operación 

"""
