from __future__ import annotations
from component import Component

from warnings import warn

class Location:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.level: int = 0
        self.locations: list[Location] = []
        self.components: list[Component] = []


    def add_location(self, location: Location) -> None:
        """Adds a Location as a subordinate of self"""
        if not isinstance(location, Location):
            raise TypeError('Passed argument is not instance of Location') from None
        elif self == location:
            raise TypeError('Can\'t pass self as argument') from None

        location.level = self.level + 1
        location.__update_hierarchy()

        self.locations.append(location)


    def add_component(self, component: Component):
        if not isinstance(component, Component):
            raise TypeError('Passed argument is not instance of Location') from None
        if component in self.components:
            warn(f'Component {component.name} is being added twice to the same location')
        self.components.append(component)


    def evaluate_location_state(self):  
        pass


    def __update_hierarchy(self):
        for l in self.locations:
            l.level = self.level + 1
            l.__update_hierarchy()