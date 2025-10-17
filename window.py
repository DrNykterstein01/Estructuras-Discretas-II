import tkinter as tk
from tkinter import ttk, messagebox

class app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tree Weaver")
        self.ventana.geometry("700x500")
        frame1 = tk.Frame(self.ventana, bg= "SlateBlue1", bd=10, relief="ridge", width=700, height=150)
        frame2 = tk.Frame(self.ventana, bg= "LightPink1", bd=10, relief="ridge", width=700, height=350)
        frame1.pack(expand=True, fill="both")
        frame2.pack(expand=True, fill="both")
        self.botonKruskal = tk.Button(self.ventana, text="Arbol Optimo (Kruskal)", command=self.mostrarGrafico, fg="black", bg="khaki1", relief="flat")
        self.botonKruskal.place(x=20, y=60)
        self.botonPrim = tk.Button(self.ventana, text="Arbol Optimo (Prim)", command=self.Listado, fg="black", bg="khaki1", relief="flat")
        self.botonPrim.place(x=600, y=60)
        self.botonAnch = tk.Button(self.ventana, text="Recorrido en Anchura", command=self.Listado, fg="black", bg="khaki1", relief="flat")
        self.botonAnch.place(x=600, y=60)
        self.botonProf = tk.Button(self.ventana, text="Busqueda en Profundidad", command=self.Listado, fg="black", bg="khaki1", relief="flat")
        self.botonProf.place(x=600, y=60)
        self.botonModPond = tk.Button(self.ventana, text="Modificar Ponderaciones", command=self.ModPond, fg="black", bg="khaki1", relief="flat")
        self.botonModPond.place(x=20, y=60)
        self.botonModAr = tk.Button(self.ventana, text="Modificar Arista", command=self.Calcular, fg="black", bg="khaki1", relief="flat")
        self.botonModAr.place(x=20, y=60)


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