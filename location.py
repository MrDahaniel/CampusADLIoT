from __future__ import annotations
from component import Component, ComponentType
from sensor import Sensor

from warnings import warn
from enum import Enum

class Location:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.level: int = 0
        self.locations: list[Location] = []
        self.components: list[Component] = []
        self.state: LocationState = LocationState.UNINITIALIZED

    def add_location(self, location: Location) -> None:
        """Adds a Location as a subordinate of self"""
        if not isinstance(location, Location):
            raise TypeError('Passed argument is not instance of Location') from None
        elif self == location:
            raise TypeError('Can\'t pass self as argument') from None

        location.level = self.level + 1
        location.__update_hierarchy()

        self.locations.append(location)


    def add_component(self, component: Component, type: ComponentType):
        if not isinstance(component, Component):
            raise TypeError('Passed argument is not instance of Location') from None
        if not isinstance(type, ComponentType):
            raise TypeError('Passed argument \'type\' is not instance of ComponentType') from None
        if component in self.components:
            warn(f'Component {component.name} is being added twice to the same location')

        component.type = type
        self.components.append(component)


    def get_components(self) -> list[Component]:
        components: list[Component] = self.components.copy()

        for loc in self.locations:
            components.extend(loc.get_components())

        return components
    

    def get_sensors(self) -> list[Sensor]:
        sensors: list[Sensor] = [sensor for component in self.components for sensor in component.sensors]

        for loc in self.locations:
            sensors.extend(loc.get_sensors())

        return sensors


    def evaluate_location_state(self) :
        all_components = self.get_components()
        all_sensors = self.get_sensors()

        for component in all_components:
            pass


        pass


    def __update_hierarchy(self):
        for l in self.locations:
            l.level = self.level + 1
            l.__update_hierarchy()


class LocationState(Enum):
    COHERENT = 'COHERENT'
    DEGRADATED = 'DEGRADATED'
    CRITICAL = 'CRITICAL'
    FAULT = 'FAULT'    
    UNINITIALIZED = 'UNINITIALIZED'
