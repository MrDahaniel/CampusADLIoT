# from graphviz import render

from location import Location
from component import Component, ComponentType
from campus import Campus

aggr: Campus = Campus()

campus: Location = Location('Campus Central', 'CampusCentral')
lp: Location = Location('Laboratorios Pesados', 'LabP')
camilo: Location = Location('Camilo Torres', 'CamiloTorres')
mecanica: Location = Location('Mecánica', 'Mecanica')

campus.add_location(lp)
campus.add_location(mecanica)
campus.add_location(camilo)

aggr.add_location(campus)
aggr.add_location(lp)
aggr.add_location(mecanica)
aggr.add_location(camilo)

pm: Component = Component('Particle Component')
pm.add_component(Component('PM10'))
pm.add_component(Component('PM2.5'))

dol139: Component = Component('DOL139')
dol139.add_component(Component('Temperature Sensor'))
dol139.add_component(Component('CO2 Sensor'))
dol139.add_component(Component('Humidity Sensor'))

climate: Component = Component('Climate Component')
climate.add_component(dol139)
climate.add_component(Component('Ammonia Sensor'))

noise: Component = Component('Noise Sensor')

alarm: Component = Component('Alarma')
alarm.add_component(Component('Sirena'))
alarm.add_component(Component('Luces'))

aggr.add_component(climate, ComponentType.MANDATORY, campus)

aggr.add_component(pm, ComponentType.OPTIONAL, camilo)
aggr.add_component(pm, ComponentType.OPTIONAL, mecanica)
aggr.add_component(pm, ComponentType.OPTIONAL, lp)

aggr.add_component(alarm, ComponentType.MANDATORY, camilo)
aggr.add_component(alarm, ComponentType.MANDATORY, mecanica)
aggr.add_component(alarm, ComponentType.MANDATORY, lp)

aggr.add_component(noise, ComponentType.OPTIONAL, mecanica)


aggr.to_graph().render('ignore/diagram', format='png')