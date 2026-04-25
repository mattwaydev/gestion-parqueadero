from datetime import datetime
import math
from operator import truediv
import random
import vehiculo


class Parqueadero:
    def __init__(self):
        #listas principales
        self.placas = []
        self.horas_ingreso = []
        self.espacio = []
        self.historial_pagos = []

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
        if vehiculo.placa in self.placas:
            return f"El vehículo {vehiculo.placa} ya está registrado en el parqueadero"
        self.placas.append(vehiculo.placa) #agrego la placa a la lista
        vehiculo.hora_ingreso = datetime.now() #aca llamo a la libreria que importe para que me dé la hora exacta de ingreso
        self.horas_ingreso.append(vehiculo.hora_ingreso) #y agrego la hora a la lista

        if vehiculo.movilidad_reducida:
            for clave in random.sample(list(self.espacios_parqueadero.keys()), len(self.espacios_parqueadero)):
                valor = self.espacios_parqueadero[clave]
                if not valor and "MR" in clave: #valido que el espacio si está libre
                    self.espacios_parqueadero[clave] = True
                    vehiculo.espacio = clave
                    self.espacio.append(clave)
                    break

        else:

            for clave in random.sample(list(self.espacios_parqueadero.keys()), len(self.espacios_parqueadero)):
                valor = self.espacios_parqueadero[clave]
                if not valor: #valido que el espacio si está libre
                    if vehiculo.tipo == "auto" and clave[2] in ["G", "H", "I", "J"]:
                        self.espacios_parqueadero[clave] = True #marco el espacio como ocupado en el diccionario
                        vehiculo.espacio = clave #le digo al vehículo en que espacio quedó parqueado
                        self.espacio.append(clave) #agrego ese espacio a la lista de espacios asignados
                        break
            for clave in random.sample(list(self.espacios_parqueadero.keys()), len(self.espacios_parqueadero)):
                valor = self.espacios_parqueadero[clave]
                if not valor: #valido que el espacio si está libre
                    if vehiculo.tipo == "moto" and clave[2] in ["A", "B", "C", "D", "E", "F"]:
                        self.espacios_parqueadero[clave] = True
                        vehiculo.espacio = clave
                        self.espacio.append(clave)
                        break

        if vehiculo.espacio is None:
            self.placas.remove(vehiculo.placa)
            self.horas_ingreso.pop(-1)
            return "No hay espacios disponibles para este tipo de vehículo"
        return "Vehículo registrado exitosamente"


    def retirar_vehiculo(self, placa):
        if placa not in self.placas:
            return f"El placa {placa} no se encuentra en el parqueadero"
        indice = self.placas.index(placa)
        espacio = self.espacio[indice]
        hora_ingreso = self.horas_ingreso[indice]

        hora_salida = datetime.now() #aca solo capturo la hora actual de salida
        diferencia = hora_salida - hora_ingreso #resto las dos horas y me da la diferencia
        horas = diferencia.total_seconds() / 3600 #aca simplemente convierto de segundos a horas
        total = math.ceil(horas) * 2000 #con esto solo redondeo las horas, es decir redondea hacia arriba (fracción de hora = hora completa)

        #ahora hay que liberar el espacio y eliminar el vehiculo de las 3 listas

        self.espacios_parqueadero[espacio] = False
        self.placas.remove(placa)
        self.espacio.remove(espacio)
        self.horas_ingreso.pop(indice)

        #utlizo remove en una porque busca el valor y lo elimina, pop elimina por posición, lo usamos en horas porque la hora no es un valor único fácil de buscar

        self.historial_pagos.append(f"{placa} - ${total} - {hora_salida.strftime('%H:%M:%S')}")

        return (f"Vehículo {placa} retirado. Total a pagar: ${total}")

    def consultar_vehiculo(self, placa):
        try:
            indice = self.placas.index(placa) #busco en la lista de placas, donde esta esa placa
            espacio = self.espacio[indice] #con ese indice, va a la lista de espacios y saca el espacio que me corresponde
            return f"El vehículo {placa} está en el espacio: {espacio}"
        except ValueError:
            return f"El vehículo {placa} no se encuentra en el parqueadero"

    def consultar_piso(self, piso):

        """
            la linea 89 recorre la lista de espacios.
            enumerate es especial porque te da dos cosas a la vez: el índice i y el valor espacio.
            Lo necesitamos porque con el índice podemos buscar la placa correspondiente.
            """
        vehiculos_piso = [] #crearé una lista vacia para guardar las placas que encuentre en cierto piso
        for i, espacio in enumerate(self.espacio):
            if espacio.startswith(f"P{piso}"): #verifica si el espacio pertenece al piso que buscamos, si buscas piso 1, revisa el espacio empiza con "p1"
                vehiculos_piso.append(self.placas[i]) #si el espacio es del piso buscado, agrega la placa correspondiente a la lista
        if not vehiculos_piso:
            return f"No hay vehículos en el piso {piso}"
        else:
            return f"Vehículos en el piso {piso}: {', '.join(vehiculos_piso)}" #join une los elementos de una lista en un solo texto, separándolos con lo que le pongo

    def estadisticas(self):
        motos_libres = 0
        motos_ocupadas = 0
        autos_libres = 0
        autos_ocupadas = 0
        mr_libres = 0
        mr_ocupadas = 0

        for clave, ocupado in self.espacios_parqueadero.items():
            if "MR" in clave:
                if ocupado:
                    mr_ocupadas += 1
                else:
                    mr_libres += 1
            elif clave[2] in ["A", "B", "C", "D", "E", "F"]:
                if ocupado:
                    motos_ocupadas += 1
                else:
                    motos_libres += 1
            else:
                if ocupado:
                    autos_ocupadas += 1
                else:
                    autos_libres += 1
        return (f"MOTOS: {motos_libres} libres, {motos_ocupadas} ocupadas\n"
                f"AUTOS: {autos_libres} libres, {autos_ocupadas} ocupadas\n"
                f"MOVILIDAD REDUCIDA: {mr_libres} libres, {mr_ocupadas} ocupadas")




    def buscar_por_tipo(self, tipo):
        resultado = []
        for i, espacio in enumerate(self.espacio):
            if tipo == "moto" and espacio[2] in ["A", "B", "C", "D", "E", "F"]:
                resultado.append(f"{self.placas[i]} - {espacio}")
            elif tipo == "auto" and espacio[2] in ["G", "H", "I", "J"]:
                resultado.append(f"{self.placas[i]} - {espacio}")
            elif tipo == "mr" and "MR" in espacio:
                resultado.append(f"{self.placas[i]} - {espacio}")

        if not resultado:
            return f"No hay vehículos de tipo  '{tipo}' parqueados"
        return "\n".join(resultado)

    def reporte_ingresos(self):
        if not self.historial_pagos:
            return "No hay ingresos registrados aún"

        total = sum([int(p.split("$")[1].split(" ")[0]) for p in self.historial_pagos])
        pagos = [int(p.split("$")[1].split(" ")[0]) for p in self.historial_pagos]

        return (f"Total vehículos atendidos: {len(self.historial_pagos)}\n"
                f"Total recaudado: ${total}\n"
                f"Pago más alto: ${max(pagos)}\n"
                f"Pago más bajo: ${min(pagos)}")




