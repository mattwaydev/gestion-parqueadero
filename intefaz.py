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
        ctk.CTkLabel(self.panel_menu, text="─────────────", font=("Arial", 8)).pack(pady=5)
        ctk.CTkButton(self.panel_menu, text="Administrador", command=self.mostrar_admin).pack(pady=5, padx=10, fill="x")
        ctk.CTkLabel(self.panel_menu, text="─────────────", font=("Arial", 8)).pack(pady=5)
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
        resultado = self.parqueadero.registrar_vehiculo(v)
        messagebox.showinfo("Resultado", resultado)

    def mostrar_retiro(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.panel_contenido, text="Retirar vehículo", font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkLabel(self.panel_contenido, text="Placa:").pack()
        self.entry_placa_retiro = ctk.CTkEntry(self.panel_contenido, placeholder_text="Ej: ABC123")
        self.entry_placa_retiro.pack(pady=5)

        ctk.CTkButton(self.panel_contenido, text="Retirar", command=self.retirar).pack(pady=10)

    def retirar(self):
        placa = self.entry_placa_retiro.get()
        if not placa:
            messagebox.showerror("Error", "Ingresa una placa")
            return
        resultado = self.parqueadero.retirar_vehiculo(placa)
        messagebox.showinfo("Pago", resultado)

    def mostrar_consulta(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.panel_contenido, text="Consultar", font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkLabel(self.panel_contenido, text="Buscar por placa:").pack()
        self.entry_placa_consulta = ctk.CTkEntry(self.panel_contenido, placeholder_text="Ej: ABC123")
        self.entry_placa_consulta.pack(pady=5)
        ctk.CTkButton(self.panel_contenido, text="Buscar vehículo", command=self.consultar_vehiculo).pack(pady=5)

        ctk.CTkLabel(self.panel_contenido, text="Buscar por piso:").pack(pady=10)
        self.entry_piso = ctk.CTkEntry(self.panel_contenido, placeholder_text="1, 2 o 3")
        self.entry_piso.pack(pady=5)
        ctk.CTkButton(self.panel_contenido, text="Ver vehículos del piso", command=self.consultar_piso).pack(pady=5)

    def consultar_vehiculo(self):
        placa = self.entry_placa_consulta.get()
        if not placa:
            messagebox.showerror("Error", "Ingresa una placa")
            return
        resultado = self.parqueadero.consultar_vehiculo(placa)
        messagebox.showinfo("Resultado", resultado)

    def consultar_piso(self):
        piso = self.entry_piso.get()
        if not piso:
            messagebox.showerror("Error", "Ingresa un piso")
            return
        resultado = self.parqueadero.consultar_piso(int(piso))
        messagebox.showinfo("Resultado", resultado)

    def mostrar_mapa(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.panel_contenido, text="Mapa del parqueadero", font=("Arial", 18, "bold")).pack(pady=10)

        # Selector de piso
        self.piso_mapa = ctk.StringVar(value="1")
        frame_piso = ctk.CTkFrame(self.panel_contenido)
        frame_piso.pack(pady=5)
        ctk.CTkLabel(frame_piso, text="Piso:").pack(side="left", padx=5)
        ctk.CTkRadioButton(frame_piso, text="1", variable=self.piso_mapa, value="1", command=self.dibujar_mapa).pack(
            side="left", padx=5)
        ctk.CTkRadioButton(frame_piso, text="2", variable=self.piso_mapa, value="2", command=self.dibujar_mapa).pack(
            side="left", padx=5)
        ctk.CTkRadioButton(frame_piso, text="3", variable=self.piso_mapa, value="3", command=self.dibujar_mapa).pack(
            side="left", padx=5)

        # Frame del mapa
        self.frame_mapa = ctk.CTkScrollableFrame(self.panel_contenido)
        self.frame_mapa.pack(fill="both", expand=True, padx=10, pady=10)

        self.dibujar_mapa()

    def dibujar_mapa(self):
        for widget in self.frame_mapa.winfo_children():
            widget.destroy()

        piso = self.piso_mapa.get()
        filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "MR"]

        for fila in filas:
            frame_fila = ctk.CTkFrame(self.frame_mapa)
            frame_fila.pack(fill="x", pady=2)
            ctk.CTkLabel(frame_fila, text=fila, width=30).pack(side="left", padx=5)

            if fila == "MR":
                puestos = range(1, 11)
            else:
                puestos = range(1, 21)

            for puesto in puestos:
                clave = f"P{piso}{fila}{puesto}"
                ocupado = self.parqueadero.espacios_parqueadero.get(clave, False)
                color = "#e74c3c" if ocupado else "#2ecc71"
                btn = ctk.CTkButton(frame_fila, text=str(puesto), width=35, height=25, fg_color=color,
                                    hover_color=color)
                btn.pack(side="left", padx=1)

    def mostrar_admin(self):
        for widget in self.panel_contenido.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.panel_contenido, text="Panel Administrador", font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkLabel(self.panel_contenido, text="Buscar vehículo por placa:").pack()
        self.entry_placa_admin = ctk.CTkEntry(self.panel_contenido, placeholder_text="Ej: ABC123")
        self.entry_placa_admin.pack(pady=5)
        ctk.CTkButton(self.panel_contenido, text="Buscar", command=self.admin_consultar_vehiculo).pack(pady=5)

        ctk.CTkLabel(self.panel_contenido, text="Ver vehículos por piso:").pack(pady=10)
        self.entry_piso_admin = ctk.CTkEntry(self.panel_contenido, placeholder_text="1, 2 o 3")
        self.entry_piso_admin.pack(pady=5)
        ctk.CTkButton(self.panel_contenido, text="Ver piso", command=self.admin_consultar_piso).pack(pady=5)
        ctk.CTkLabel(self.panel_contenido, text="Historial de pagos:").pack(pady=10)
        ctk.CTkButton(self.panel_contenido, text="Ver historial", command=self.ver_historial).pack(pady=5)
        ctk.CTkLabel(self.panel_contenido, text="Estadísticas:").pack(pady=10)
        ctk.CTkButton(self.panel_contenido, text="Ver estadísticas", command=self.ver_estadisticas).pack(pady=5)

    def admin_consultar_vehiculo(self):
        placa = self.entry_placa_admin.get()
        if not placa:
            messagebox.showerror("Error", "Ingresa una placa")
            return
        resultado = self.parqueadero.consultar_vehiculo(placa)
        messagebox.showinfo("Resultado", resultado)

    def admin_consultar_piso(self):
        piso = self.entry_piso_admin.get()
        if not piso:
            messagebox.showerror("Error", "Ingresa un piso")
            return
        resultado = self.parqueadero.consultar_piso(int(piso))
        messagebox.showinfo("Resultado", resultado)

    def ver_historial(self):
        historial = self.parqueadero.historial_pagos
        if not historial:
            messagebox.showinfo("Historial", "No hay pagos registrados aún")
            return
        texto = "\n".join(historial)
        messagebox.showinfo("Historial de pagos", texto)

    def ver_estadisticas(self):
        resultado = self.parqueadero.estadisticas()
        messagebox.showinfo("Estadísticas", resultado)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ElPaso(root)
    root.mainloop()