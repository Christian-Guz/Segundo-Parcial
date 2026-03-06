import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operaciones = opcion.get()
        
        if operaciones == 1:
            resultado = num1 + num2
        elif operaciones == 2:
            resultado = num1 - num2
        elif operaciones == 3:
            resultado = num1 * num2
        elif operaciones == 4:
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado = num1 / num2
        else:
            messagebox.showwarning("Advertencia", "Selecciona una operación")
            return
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa número válidos")
        
#Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora con Radiobotones")
ventana.geometry("350x300")

#Entradas
tk.Label(ventana, text = "Primer número:").grid(row=0, column=0)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1,column=1)

#Variable para los radiobotones
opcion = tk.IntVar()

tk.Label(ventana, text="Selecciona la operación:").grid(row=2, column=1)

tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).grid(row=3, column=0, sticky="w")
tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).grid(row=3, column=1)
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).grid(row=4, column=0)
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).grid(row=4, column=1)

#Botón calcular
tk.Button(ventana, text="Calcular", command=calcular).grid(row=5, column=1)

#Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.grid(row=6, column=1)

ventana.mainloop()