import tkinter as tk

def saludo():
    label_resultado.config(text = "Hola alumnos de Python") #Es este de aca



ventana = tk.Tk()
ventana.title("Ejemplo con botones")
ventana.geometry("400x300")

#Creamos el boton
boton = tk.Button(ventana, text="Saludar", command = saludo) #Este de aquí
boton.pack(pady=20)

#Creamos una etiqueta
label_resultado = tk.Label(ventana, text="",
                    font=("Arial",16,"bold"))
label_resultado.pack(pady=20)

#Mostramos la etiqueta en la ventana
ventana.mainloop()
