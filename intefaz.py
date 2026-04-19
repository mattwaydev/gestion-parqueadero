import customtkinter as ctk
from tkinter import messagebox
from parqueadero import Parqueadero
from vehiculo import Vehiculo


class ElPaso:
    def __init__(self, root):
        self.root = root
        self.root.title("El Paso")
        self.root.geometry("900x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.parqueadero = Parqueadero()
        self.crear_layout()

    def crear_layout(self):
        self.panel_menu = ctk.CTkFrame(self.root, width=200, corner_radius=0)
        self.panel_menu.pack(side="left", fill="y")
        self.panel_contenido = ctk.CTkFrame(self.root)
        self.panel_contenido.pack(side="right", fill="both", expand=True)
        ctk.CTkLabel(self.panel_menu, text="El Paso", font=("Arial", 20, "bold")).pack(pady=20)
        ctk.CTkLabel(self.panel_menu, text="GG, encontraste parqueadero", font=("Arial", 9), wraplength=180).pack()
        ctk.CTkButton(self.panel_menu, text="Registrar vehículo", command=self.mostrar_registro).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.panel_menu, text="Retirar vehículo", command=self.mostrar_retiro).pack(pady=5, padx=10, fill="x")
        ctk.CTkButton(self.panel_menu, text="Consultar vehículo", command=self.mostrar_consulta).pack(pady=5, padx=10, fill="x")
        ctk.CTkButton(self.panel_menu, text="Ver mapa", command=self.mostrar_mapa).pack(pady=5, padx=10, fill="x")

    def mostrar_registro(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.panel_contenido, text="Registrar vehículo", font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkLabel(self.panel_contenido, text="Placa:").pack()
        self.entry_placa = ctk.CTkEntry(self.panel_contenido, placeholder_text="Ej: ABC123")
        self.entry_placa.pack(pady=5)

        ctk.CTkLabel(self.panel_contenido, text="Tipo de vehículo:").pack()
        self.tipo_var = ctk.StringVar(value="auto")
        ctk.CTkRadioButton(self.panel_contenido, text="Auto", variable=self.tipo_var, value="auto").pack()
        ctk.CTkRadioButton(self.panel_contenido, text="Moto", variable=self.tipo_var, value="moto").pack()

        self.mr_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(self.panel_contenido, text="Movilidad reducida", variable=self.mr_var).pack(pady=10)

        ctk.CTkButton(self.panel_contenido, text="Registrar", command=self.registrar).pack(pady=10)

    def registrar(self):
        placa = self.entry_placa.get()
        tipo = self.tipo_var.get()
        mr = self.mr_var.get()

        if not placa:
            messagebox.showerror("Error", "Ingresa una placa")
            return

        v = Vehiculo(placa, tipo, mr)
        self.parqueadero.registrar_vehiculo(v)
        messagebox.showinfo("Éxito", f"Vehículo {placa} registrado en {v.espacio}")

    def mostrar_retiro(self):
        pass

    def mostrar_consulta(self):
        pass

    def mostrar_mapa(self):
        pass


if __name__ == "__main__":
    root = ctk.CTk()
    app = ElPaso(root)
    root.mainloop()