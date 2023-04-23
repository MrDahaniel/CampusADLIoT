# from campus import Campus
from location import Location
from component import Component
from sensor import Sensor

campus: Location = Location('campus')
location_a: Location = Location('A')
location_b: Location = Location('B')
location_b2: Location = Location('B2')

pm: Component = Component('Particle Component')

pm10: Sensor = Sensor('PM10 Sensor')
pm25: Sensor = Sensor('PM2.5 Sensor')

campus.add_location(location_a)
location_a.add_location(location_b)
location_a.add_location(location_b2)

pm.add_sensor(pm10)
pm.add_sensor(pm25)

campus.add_component(pm)


