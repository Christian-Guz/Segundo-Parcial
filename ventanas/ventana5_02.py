import tkinter as tk

ventana = tk.Tk()
ventana.title("Grid Layout")

tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(ventana).grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(ventana, show="*").grid(row=1, column=1, padx=5, pady=5)

tk.Button(ventana, text="Login").grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()