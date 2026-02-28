import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text = f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresar números válidos") #El primero es el título, el segundo es el texto

#Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x200")

#Etiquetas y entradas
tk.Label(ventana,text="Primer número:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo número:").pack(pady=5)
entrada2=tk.Entry(ventana)
entrada2.pack()

#Boton para sumar
tk.Button(ventana, text="Sumar", command = sumar).pack(pady=10)

#Etiquetas para mostrar resultado
etiqueta_resultado = tk.Label(ventana,text="Resultado: ")
etiqueta_resultado.pack()

ventana.mainloop()