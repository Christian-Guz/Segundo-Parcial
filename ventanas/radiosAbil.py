import tkinter as tk

def deshabilitar():
    radio1.config(state="disabled")
    
def habilitar():
    radio1.config(state="normal")
    
ventana = tk.Tk()
ventana.title("Control de Radiovutton")
ventana.geometry("300x200")

opcion = tk.IntVar()

radio1 = tk.Radiobutton(ventana, text="Opción1", variable=opcion, value=1)
radio1.pack(pady=10)

tk.Button(ventana, text="Deshabilitar", command=deshabilitar).pack(pady=5)
tk.Button(ventana, text="Habilitar", command=habilitar).pack(pady=5)

ventana.mainloop()