class Vehiculo:
    def __init__(self, placa, tipo, movilidad_reducida):
        self.placa = placa
        self.tipo = tipo
        self.movilidad_reducida = movilidad_reducida
        self.espacio = None
        self.hora_ingreso = None


    def __str__(self):
        return f"Placa: {self.placa} | Tipo: {self.tipo} | Espacio: {self.espacio} | Ingreso: {self.hora_ingreso}"
