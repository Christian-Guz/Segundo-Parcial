import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#PROCESO DE CÓDIGO

def calculo():
    total = 0
    por = 0
    try:
        Compradores = int(Cant_Comp.get())
        valor_max = Compradores * 7
        num_voletos = int(Cant_Bol.get())
        total=num_voletos * 12
        opc = Opcion_Tarjeta.get()
        if Compradores <= 0 or num_voletos <= 0:
            messagebox.showerror("Error", "Se ha ingresado un valor de forma erronea...")
            return
        if num_voletos > valor_max:
            messagebox.showerror("Error", "La cantidad de boletos es mayor a la permitida...")
            return
        else:
            if num_voletos > 5:
                por = total * .15
                total = total - por
            elif num_voletos >= 3 and num_voletos <= 5:
                por = total * .10
                total = total - por
        if opc == 1:
            por = total * .10
            total = total - por
        elif opc == 2:
            total = total
        else:
            messagebox.showerror("Error", "No se ha ingresado si cuenta con una tarjeta Cineco...")
            return
        Valor_Pagar.config(text=f"${total}")
    except ValueError:
        messagebox.showerror("Error", "Uno de los datos no se ha registrado...")
        return
    
#Cabina de salida
def salir():
    salida = messagebox.askyesno("Salir", "¿Desea salir del promgrama?")
    if salida:
        ventana.destroy()

#PROCESO DE CREACIÓN DE VENTANA

#Crear ventana
ventana = tk.Tk()
ventana.title("Cinepolis")
ventana.geometry("1200x666")

#Crear imágen
imagen = Image.open("cinepolis.jpg") #Llmar imagen
fondo = ImageTk.PhotoImage(imagen) #Generar imagaen en formato Tk

#Crear imagen como etiqueta (Con la intención de manipularlo com tal)
imagen_fondo = tk.Label(ventana, image=fondo)
imagen_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#Crear etiqueta de título
titulo = tk.Label(ventana, text="Cinépolis", bg="#13216A", fg="white", font=("Arial", 30, "bold", "italic"))
titulo.pack(pady=20)

#Crear primer frame y atributos (Entradas)
entradas = tk.LabelFrame(ventana, text="Entradas", bg="#13216A", fg="white", font=("Times New Roman", 30, "bold", "italic"))
entradas.place(x=100, y=100, width=450, height=180)

nom = tk.Label(entradas, text="Nombre:", bg="#13216A", fg="white", font=("Times New Roman", 15, "bold")).grid(row=0, column=0) #Etiqueta
nom_usua = tk.Entry(entradas, font=("Arial", 13)) #Cuadro de entrada de texto
nom_usua.grid(row=0, column=1)

Etiq_Comp = tk.Label(entradas, text="Cantidad de compradores:", bg="#13216A", fg="white", 
                     font=("Times New Roman", 15, "bold")).grid(row=1, column=0, padx=10) #Texto de clientes
Cant_Comp = tk.Entry(entradas, font=("Arial", 13))
Cant_Comp.grid(row=1, column=1)

Tarjeta_Cin = tk.Label(entradas, text="Tarjeta Cineco:", bg="#13216A", fg="white", 
                       font=("Times New Roman", 15, "bold")).grid(row=2, column=0) #Texto de opciones
Opcion_Tarjeta = tk.IntVar()
tk.Radiobutton(entradas, text="Si", variable=Opcion_Tarjeta, value=1, bg="#5E74E0", fg="black").grid(row=2, column=1, sticky="w", padx=30)
tk.Radiobutton(entradas, text="No", variable=Opcion_Tarjeta, value=2, bg="#5E74E0", fg="black").grid(row=2, column=1, sticky="e", padx=30)

Etiq_Bolet = tk.Label(entradas, text="Cantidad de Boletos:", bg="#13216A", fg="white",
                      font=("Times New Roman", 15, "bold")).grid(row=3, column=0)
Cant_Bol = tk.Entry(entradas, font=("Arial", 13))
Cant_Bol.grid(row=3, column=1)

#Crear segundo frame y atributos (Salidas)
salidas = tk.LabelFrame(ventana, text="Salidas", bg="#13216A", fg="white", font=("Times New Roman", 30, "bold", "italic"))
salidas.place(x= 650, y=120, width=450, height=140)
tk.Label(salidas, text="Valor a Pagar:", bg="#13216A", fg="white",
                    font=("Times New Roman", 15, "bold")).grid(row=0, column=0, padx=50, pady=20)
Valor_Pagar = tk.Label(salidas, text="", bg="#13216A", fg="white", font=("Arial", 18, "bold"))
Valor_Pagar.grid(row=0, column=1)

#Crear tercer frame y atributos (acciones)
acciones = tk.LabelFrame(ventana, text="Acciones", bg="#13216A", fg="white", font=("Times New Roman", 30, "bold", "italic"))
acciones.place(x=450, y=450, width=350, height=140)
procesar = tk.Button(acciones, command=calculo, text="Procesar", font=("Arial", 12, "bold"))
procesar.grid(row=0, column=0, padx=70, pady=20)
salir = tk.Button(acciones, text="Salir", command=salir, font=("Arial", 12, "bold"))
salir.grid(row=0, column=1)

ventana.mainloop()
