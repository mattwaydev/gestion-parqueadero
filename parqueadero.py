from datetime import datetime
import math
from operator import truediv

import vehiculo


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

    def registrar_vehiculo(self, vehiculo):
        self.placas.append(vehiculo.placa) #agrego la placa a la lista
        vehiculo.hora_ingreso = datetime.now() #aca llamo a la libreria que importe para que me la hora exacta de ingreso
        self.horas_ingreso.append(vehiculo.hora_ingreso) #y agrego la hora a la lista

        for clave, valor in self.espacios_parqueadero.items():
            if not valor: #si esta libre
                if vehiculo.tipo == "auto" and clave[2] in ["G", "H", "I", "J"]:
                    self.espacios_parqueadero[clave] = True #marco el espacio como ocupado en el diccionario
                    vehiculo.espacio = clave #le digo al vehiculo en que espacio quedó parqueado
                    self.espacio.append(clave) #agrego ese espacio a la lista de espacios asignados
                    break
        for clave, valor in self.espacios_parqueadero.items():
            if not valor:
                if vehiculo.tipo == "moto" and clave[2] in ["A", "B", "C", "D", "E", "F"]:
                    self.espacios_parqueadero[clave] = True
                    vehiculo.espacio = clave
                    self.espacio.append(clave)
                    break
        for clave, valor in self.espacios_parqueadero.items():
            if not valor:
                if vehiculo.movilidad_reducida and "MR" in clave:
                    self.espacios_parqueadero[clave] = True
                    vehiculo.espacio = clave
                    self.espacio.append(clave)
                    break
    def retirar_vehiculo(self, placa):
        indice = self.placas.index(placa)
        espacio = self.espacio[indice]
        hora_ingreso = self.horas_ingreso[indice]

        hora_salida = datetime.now() #aca solo capturo la hora actual de salida
        diferencia = hora_salida - hora_ingreso #resto las dos horas y me da la diferencia
        horas = diferencia.total_seconds() / 3600 #aca simplemente convierto de segundos a horas
        total = math.ceil(horas) * 2000 #con esto solo redondeo todo, es decir redondea hacia arriba (fracción de hora = hora completa)

        #ahora hay que liberar el espacio y eliminar el vehiculo de las 3 listas

        self.espacios_parqueadero[espacio] = False
        self.placas.remove(placa)
        self.espacio.remove(espacio)
        self.horas_ingreso.pop(indice)

        #utlizo remove en una porque busca el valor y lo elimina, pop elimina por posición, lo usamos en horas porque la hora no es un valor único fácil de buscar

        print(f"Vehículo {placa} retirado. Total a pagar: ${total}")







