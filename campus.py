# from location import Location
from component import Component
from typing import Optional


class Campus:
    def __init__(self) -> None:
        self.components: list[Component] = []
        self.locations: list[str] = []


    def add_component(self, component: Component, location_identifier: Optional[str]):
        pass

    def to_graph(self):
        seen_locations: set = set(self.locations)
        for component in self.components:
            