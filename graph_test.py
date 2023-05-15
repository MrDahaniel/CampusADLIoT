# from graphviz import render

from location import Location
from component import Component, ComponentType
from sensor import Sensor

campus: Location = Location('Campus Central')
lp: Location = Location('Laboratorios Pesados')

lp104: Location = Location('Salón 104')
oficina: Location = Location('Oficina')

centic: Location = Location('CENTIC')
camilo: Location = Location('Camilo Torres')
mecanica: Location = Location('Mecanica')

pm: Component = Component('Particle Component')
pm10: Sensor = Sensor('PM10 Sensor')
pm25: Sensor = Sensor('PM2.5 Sensor')

temp: Component = Component('Temperature Component')
# t_sens: Sensor = Sensor('Temperature Sensor')

noise: Component = Component('Noise Component')
noise_sens: Sensor = Sensor('dB Sensor')

campus.add_location(lp)
campus.add_location(mecanica)
campus.add_location(centic)
campus.add_location(camilo)

lp.add_location(lp104)
lp.add_location(oficina)

# pm.add_sensor(pm10)
# pm.add_sensor(pm25)

# # temp.add_sensor(t_sens)

# noise.add_sensor(noise_sens)

lp.add_component(pm, ComponentType.MANDATORY)

campus.add_component(temp, ComponentType.MANDATORY)
campus.add_component(noise, ComponentType.OPTIONAL)

mecanica.add_component(temp, ComponentType.MANDATORY)

campus.export('ignore/diagram')