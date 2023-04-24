# from campus import Campus
from location import Location
from component import Component, ComponentType

from sensor import Sensor

campus: Location = Location('campus')
location_a: Location = Location('A')
location_b: Location = Location('B')
location_b2: Location = Location('B2')

pm: Component = Component('Particle Component')
pm10: Sensor = Sensor('PM10 Sensor')
pm25: Sensor = Sensor('PM2.5 Sensor')

temp: Component = Component('Temperature Component')
t_sens: Sensor = Sensor('Temperature Sensor')

noise: Component = Component('Noise Component')
noise_sens: Sensor = Sensor('dB Sensor')

campus.add_location(location_a)
location_a.add_location(location_b)
location_a.add_location(location_b2)

pm.add_sensor(pm10)
pm.add_sensor(pm25)

temp.add_sensor(t_sens)

noise.add_sensor(noise_sens)

location_a.add_component(pm, ComponentType.MANDATORY)

location_b.add_component(temp, ComponentType.MANDATORY)
location_b2.add_component(noise, ComponentType.OPTIONAL)


print('Components:')
for i in campus.get_components():
    print(f'{i.name}: {i.type}')

print('\nSensors:')
for i in campus.get_sensors():
    print(i.name)