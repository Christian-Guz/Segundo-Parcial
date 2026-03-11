import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

#PORCESO DE FUNCIONAMIENTO
def proceso():
    x=0
    y= 0
    total = 0
    combos_1 = combo1.get()
    combos_2 = combo2.get()
    combos_3 = combo3.get()
    tolerancia = tol.get()
    for opcion in colores:
        if opcion == colores[0]: #Definición del color en caso de ser color negro, cambiará a blanco
            c = "white"
        else:
            c= "black"
        if opcion == combos_1:
            tk.Label(ventana, bg=f"{color_pin[x]}", fg=c, text=f"{x}", 
                     font=("Arial", 12, "bold")).place(x=280, y=355, height=30, width=100)
            p1 = x * 10
            y+=1
        if opcion == combos_2:
            tk.Label(ventana, bg=f"{color_pin[x]}", fg=c, text=f"{x}", 
                     font=("Arial", 12, "bold")).place(x=280, y=425, height=30, width=100)
            p2 = x
            y+=1
        if opcion == combos_3:
            n0 = "0" * x
            p3 = int("1" + n0)
            y+=1
            tk.Label(ventana, bg=f"{color_pin[x]}", fg=c, text=f"{p3}", 
                     font=("Arial", 12, "bold")).place(x=280, y=495, height=30, width=100)
        x+=1
    if y == 0 or y < 3:
        messagebox.showerror("Error", "Uno de los colores no ha sido seleccionado")
        return
    if tolerancia == 1:
        t = "#D4C51C"
        porc = .05
    else:
        t = "#A9A9A7"
        porc = .10
    if tolerancia == 1 or tolerancia == 2:
        tk.Label(ventana, bg=t).place(y=570, x=200, height=30, width=75)
    else:
        messagebox.showerror("Error", "No se ha seleccionado un valor de tolerancia")
        return
    potencia = (p1 + p2) * p3
    tol_dif = porc * potencia
    tol_max = potencia + tol_dif
    tol_min = potencia - tol_dif
    val_ohm.config(text=potencia)
    val_max.config(text=tol_max)
    val_min.config(text=tol_min)

#DISEÑO DE VENTANA

#Creación de ventana principal
ventana = tk.Tk()
ventana.geometry("500x750")
fondo = tk.Label(ventana, bg="#7CBEDE").place(x=0, y=0, height=750, width=500)

#Creación del cuadro de título
titulo = tk.Label(ventana, text="Calcular Valores de Resistencia", bg="#A0BC32", fg="white", 
                  font=("Time New Roman", 15, "bold", "italic")).place(y=10, x=10, height=85, width=480)

#Creación de la imágen
imagen = Image.open("Resistencia.jpg")
imagen_ = ImageTk.PhotoImage(imagen)
imagen_cuadro = tk.Label(ventana, image=imagen_)
imagen_cuadro.place(x=90, y=100, width=320, height=241)

#Creación de las listas
colores = ["Negro", "Café", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]
color_pin = ["#1E1A17", "#CA8152", "#FD0005", "#E97918", "#FDF205", "#05FF04", "#0B4FF1", "#984277", "#848181", "#FFFFFF"]

#Creación de los combos
combo1 = ttk.Combobox(ventana, values=colores)
combo1.place(y=360, x=95)
combo1.set("Seleccione el Color 1")

combo2 = ttk.Combobox(ventana, values=colores)
combo2.place(y=430, x=95)
combo2.set("Seleccione el Color 2")

combo3 = ttk.Combobox(ventana, values=colores)
combo3.place(y=500, x=95)
combo3.set("Seleccione el Color 3")

#Texto de tolerancia

tk.Label(ventana, text="Tolerancia", bg="#7CBEDE", font=("Arial", 12, "bold", "italic")).place(y=535, x=95) 

#Ceración de Radio botones
tol = tk.IntVar()

tk.Radiobutton(ventana, text="Oro", bg="#7CBEDE", variable=tol, value=1).place(y=560, x=95)
tk.Radiobutton(ventana, text="Plata", bg="#7CBEDE", variable=tol, value=2).place(y=585, x=95 )

#Creación de etiquetas de valores
tk.Label(ventana, text="Valor ohm:", bg="#7CBEDE", font=("Arial", 10, "bold")).place(y=660, x=160)
tk.Label(ventana, text="Valor máximo:", bg="#7CBEDE", font=("Arial", 10, "bold")).place(y=680, x=160)
tk.Label(ventana, text="Valor mínimo:", bg="#7CBEDE", font=("Arial", 10, "bold")).place(y=700, x=160)

#Creación de valor en ohm
val_ohm = tk.Label(ventana, text="", bg="#7CBEDE", font=("Arial", 10, "bold"))
val_ohm.place(y=660, x=280)
#Valor máximo
val_max = tk.Label(ventana, text="", bg="#7CBEDE", font=("Arial", 10, "bold"))
val_max.place(y=680, x=280)
#Valor mínimo
val_min = tk.Label(ventana, text="", bg="#7CBEDE", font=("Arial", 10, "bold"))
val_min.place(y=700, x=280)

#Creación del botón del proceso completo
calcular = tk.Button(ventana, text="Calcular", bg="#B8E221", command=proceso, font=("Arial", 15, "bold"))
calcular.place(x=200, y=620, height=30, width=100)

ventana.mainloop()