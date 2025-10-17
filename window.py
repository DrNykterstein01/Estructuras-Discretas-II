import tkinter as tk
from tkinter import ttk, messagebox

class app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tree Weaver")
        self.ventana.geometry("700x500")
        frame1 = tk.Frame(self.ventana, bg= "SlateBlue1", bd=10, relief="ridge", width=700, height=150, cursor="heart")
        frame2 = tk.Frame(self.ventana, bg= "LightPink1", bd=10, relief="ridge", width=700, height=350, cursor="heart")
        frame1.pack(expand=True, fill="both")
        frame2.pack(expand=True, fill="both")
        self.botonKruskal = tk.Button(self.ventana, text="Arbol Optimo (Kruskal)", command=self.mostrarGrafico, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonKruskal.place(x=30, y=40)
        self.botonPrim = tk.Button(self.ventana, text="Arbol Optimo (Prim)", command=self.Listado, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonPrim.place(x=200, y=40)
        self.botonAnch = tk.Button(self.ventana, text="Recorrido en Anchura", command=self.Listado, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonAnch.place(x=365, y=40)
        self.botonProf = tk.Button(self.ventana, text="Busqueda en Profundidad", command=self.Listado, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonProf.place(x=525, y=40)
        self.botonModPond = tk.Button(self.ventana, text="Modificar Ponderaciones", command=self.ModPond, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonModPond.place(x=100, y=90)
        self.botonModAr = tk.Button(self.ventana, text="Modificar Arista", command=self.Calcular, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonModAr.place(x=300, y=90)
        self.botonModVer = tk.Button(self.ventana, text="Modificar Vertice", command=self.ModPond, fg="black", bg="khaki1", relief="flat", cursor="heart")
        self.botonModVer.place(x=450, y=90)


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