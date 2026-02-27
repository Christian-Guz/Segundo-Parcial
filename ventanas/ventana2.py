import tkinter as tk

ventana = tk.Tk()

ventana.title("Mu primera aplicación")

#Le damos un tamaño a la pantalla
ventana.geometry("400x300")

#Creamos una etiqueta
etiqueta = tk.Label(ventana, text="Hola Mundo",
                    font=("Arial",16,"bold"))
etiqueta.pack(pady=20)

#Mostramos la etiqueta en la ventana
ventana.mainloop()