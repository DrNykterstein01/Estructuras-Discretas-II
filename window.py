import tkinter as tk
from tkinter import ttk, messagebox

class app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tree Weaver")
        self.ventana.geometry("700x500")
        frame1 = tk.Frame(self.ventana, bg= "pink", bd=50)
        frame2 = tk.Frame(self.ventana, bg= "aquamarine", bd=50)
        frame1.pack(expand=True, fill="both")
        frame2.pack(expand=True, fill="both")
        self.botonGrafico = tk.Button(self.ventana, text="Ver Gráfico", command=self.mostrarGrafico, fg="white", bg="blue")
        self.botonGrafico.place(x=20, y=250)
        self.botonListado = tk.Button(self.ventana, text="Listado de trayectorias", command=self.Listado, fg="white", bg="blue")
        self.botonListado.place(x=180, y=250)
        self.botonModPond = tk.Button(self.ventana, text="Modificar Ponderaciones", command=self.ModPond, fg="white", bg="blue")
        self.botonModPond.place(x=340, y=250)
        self.botonCalcular = tk.Button(self.ventana, text="Calcular Ponderaciones", command=self.Calcular, fg="white", bg="blue")
        self.botonCalcular.place(x=180, y=350)


        self.ventana.mainloop()

    def mostrarGrafico(self):
        messagebox.showinfo("Gráfico", "Aquí se mostraría el gráfico.")
    
    def Listado(self):
        messagebox.showinfo("Listado", "Aquí se mostraría el listado de trayectorias.")
    
    def ModPond(self):
        messagebox.showinfo("Modificar Ponderaciones", "Aquí se modificarían las ponderaciones.")
    
    def Calcular(self):
        messagebox.showinfo("Calcular Ponderaciones", "Aquí se calcularían las ponderaciones.")
    
def main():
    objMain = app()

if __name__ == "__main__":
    main()