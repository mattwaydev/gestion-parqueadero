from parqueadero import Parqueadero
from vehiculo import Vehiculo
import time # time.sleep(2) hace que el programa espere 2 segundos para que haya una diferencia de tiempo real y el cobro no salga en $0

p = Parqueadero()
v = Vehiculo("ABC123", "auto", False)
p.registrar_vehiculo(v)
print(v)


time.sleep(2)
p.retirar_vehiculo("ABC123")