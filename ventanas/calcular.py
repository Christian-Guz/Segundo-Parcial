import tkinter as tk
from tkinter import messagebox

def suma(): #el código salta la función
    try:
        num1 = float(escritura1.get())
        num2 = float(escritura2.get())
        rest = num1 + num2
        resultado.config(text=f"Resultado: {rest}")
    except ValueError:
        messagebox.showerror("Error","Por favor, ingrese un número válido")
    

ventana = tk.Tk() #El código empieza aquí

ventana.title("Calculadora")
ventana.geometry("400x300")

#Etiquetas/Textos
texto1 = tk.Label(ventana, text = "Num1:", font = ("Arial",16,"bold"))
texto1.grid(row=0,column=0)

texto2 = tk.Label(ventana, text="Num2:", font= ("Arial",16,"bold"))
texto2.grid(row=1,column=0)

#Cuadros de entrada
escritura1 = tk.Entry(ventana, font=("Arial", 16))
escritura1.grid(row=0,column=1)

escritura2 = tk.Entry(ventana, font=("Arial",16))
escritura2.grid(row=1,column=1)

#Boton de cálculo
boton = tk.Button(ventana, text="Calcular", command = suma)
boton.grid(row=2,column=0)

#Texto de resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.grid(row=3,column=1)

ventana.mainloop()