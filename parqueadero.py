class Parqueadero:
    def __init__(self):
        #listas principales
        self.placas = []
        self.horas_ingreso = []
        self.espacio = []

        #crearé un diccionario para guardar los espacios de cada piso
        #y cada espacio lo generaré con un bucle
        self.espacios_parqueadero = {}

        for piso in range(1, 4):
            for fila in ["A", "B", "C", "D", "E", "F"]:
                for puesto in range(1, 21):
                    clave = f"P{piso}{fila}{puesto}"
                    self.espacios_parqueadero[clave] = False
            for fila in ["G", "H", "I", "J"]:
                for puesto in range(1, 21):
                    clave = f"P{piso}{fila}{puesto}"
                    self.espacios_parqueadero[clave] = False
            for puesto in range(1, 11):
                clave = f"P{piso}MR{puesto}"
                self.espacios_parqueadero[clave] = False