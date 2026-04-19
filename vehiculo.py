class Vehiculo:
    def __init__(self, placa, tipo, movilidad_reducidad):
        self.placa = placa
        self.tipo = tipo
        self.movilidad_reducidad = movilidad_reducidad
        self.espacio = None
        self.hora_ingreso = None


    def __str__(self):
        return f"Placa: {self.placa} | Tipo: {self.tipo} | Espacio: {self.espacio} | Ingreso: {self.hora_ingreso}"
