from parqueadero import Parqueadero
from vehiculo import Vehiculo

p = Parqueadero()
v = Vehiculo("ABC123", "auto", False)
p.registrar_vehiculo(v)
print(v)