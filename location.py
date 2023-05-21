from __future__ import annotations
from typing import Optional
from component import Component, ComponentType
from sensor import Sensor

from graphviz import Digraph

from warnings import warn
from enum import Enum

class Location:
    def __init__(self, name: str, identifier: str | None = None ) -> None:
        self.name: str = name
        self.level: int = 0
        self.locations: list[Location] = []
        self.location_identifier: str = identifier or name
        self.state: LocationState = LocationState.UNINITIALIZED

    def add_location(self, location: Location) -> None:
        """Adds a Location as a subordinate of self"""
        if not isinstance(location, Location):
            raise TypeError('Passed argument is not instance of Location') from None
        elif self == location:
            raise TypeError('Can\'t pass self as argument') from None

        self.locations.append(location)


class LocationState(Enum):
    COHERENT = 'COHERENT'
    DEGRADATED = 'DEGRADATED'
    CRITICAL = 'CRITICAL'
    FAULT = 'FAULT'    
    UNINITIALIZED = 'UNINITIALIZED'

    # def add_component(self, component: Component, type: ComponentType):
    #     if not isinstance(component, Component):
    #         raise TypeError('Passed argument is not instance of Location') from None
    #     if not isinstance(type, ComponentType):
    #         raise TypeError('Passed argument \'type\' is not instance of ComponentType') from None
    #     if component in self.components:
    #         warn(f'Component {component.name} is being added twice to the same location')

    #     component.type = type
    #     self.components.append(component)


    # def get_components(self) -> list[Component]:
    #     components: list[Component] = self.components.copy()

    #     for loc in self.locations:
    #         components.extend(loc.get_components())

    #     return components
    

    # def get_sensors(self) -> list[Sensor]:
    #     sensors: list[Sensor] = [sensor for component in self.components for sensor in component.sensors]

    #     for loc in self.locations:
    #         sensors.extend(loc.get_sensors())

    #     return sensors


    # def evaluate_location_state(self) :
    #     all_components = self.get_components()
    #     # all_sensors = self.get_sensors()

    #     for component in all_components:
    #         pass


    # def to_json(self):
    #     pass


    # def __update_hierarchy(self):
    #     for l in self.locations:
    #         l.level = self.level + 1
    #         l.__update_hierarchy()
    

    # def export(self, filename: str = 'diagram', format: str = 'png'):
    #     self.to_graph().render(filename = filename, format = format)


    # def _add_location_clusters(self, dot: Digraph):
    #     if not self.locations:
    #         return
        
    #     with dot.subgraph(name=f'cluster_{self.name}_locations') as sub: #type: ignore
    #         sub.attr(label='Child Locations')
    #         sub.attr(style='rounded')
    #         for location in self.locations:
    #             location._add_cluster(sub) #type: ignore
                    
    
    # def _add_component_cluster(self, dot: Digraph):
    #     with dot.subgraph(name=f'cluster_{self.name}_components') as sub: #type: ignore
    #         sub.attr(style='dotted,rounded', label='Components', labeljust='l')
    #         self._add_sensor_cluster(sub) #type: ignore

    
    # def _add_sensor_cluster(self, dot: Digraph):
    #     for component in self.components:
    #         cls_label = component.name.replace(' ', "\\n")
    #         if component.components:
    #             cluster = f'cluster_{self.name}{component.name}Sensors'.replace(' ', '')
    #             with dot.subgraph(name=cluster) as subsub: #type: ignore
    #                 subsub.attr(label = cls_label, style='dashed,rounded')
    #                 for sensor in component.components:
    #                     sensor_name = f'sensor{self.name}{component.name}{sensor.name}'.replace(' ','')
    #                     sensor_label = sensor.name.replace(' ', "\\n")
    #                     subsub.node(sensor_name, label=sensor_label)
    #                     # sensor.node_name = sensor_name
    #         else:
    #             node_name = f'{self.name}{component.name}'
    #             dot.node(node_name, label=cls_label, shape='box')
    
    # def _add_cluster(self, dot: Digraph):
    #     if self.components or self.locations:
    #         with dot.subgraph(name=f'cluster_{self.name}') as sub: #type: ignore
    #             sub.attr(label=self.name, labeljust='l')
    #             self._add_location_clusters(sub) #type: ignore
    #             self._add_component_cluster(sub) #type: ignore
    #             return
    #     dot.node(self.name.replace(' ', "\\n"), shape='box')


    # def _add_edges(self, dot: Digraph):
    #     sensors = self.get_components()
    #     for sensor, lag_sensor in zip(sensors, reversed(sensors)):
    #         dot.edge(sensor.name, lag_sensor.name)
            


    # def to_graph(self):
    #     dot = Digraph(engine = 'dot')
    #     dot.attr(style='rounded', K="2", start="1", overlap="scalexy")
    #     dot.attr('node', shape='box', style='rounded')
    #     dot.attr('edge', style='invis')
    #     self._add_cluster(dot)
    #     self._add_edges(dot)
    #     return dot
    

    # def _add_location_nodes(self, dot: Digraph):
    #     pass

    # def better_graph(self):
    #     dot = Digraph(engine = 'dot')
        



