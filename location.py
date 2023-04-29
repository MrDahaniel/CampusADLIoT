from __future__ import annotations
from component import Component, ComponentType
from sensor import Sensor

from graphviz import Digraph

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


    def to_json(self):
        pass


    def __update_hierarchy(self):
        for l in self.locations:
            l.level = self.level + 1
            l.__update_hierarchy()

    def to_digraph(self):
        dot = Digraph()
        self._add_location_clusters(dot, self)

        return dot
    
    def export(self, filename: str = 'diagram', format: str = 'png'):
        self.to_digraph().render(filename = filename, format = format)

    def _add_location_clusters(self, parent_cluster, location):
        if location.locations or location.components:
            with parent_cluster.subgraph(name=f'cluster_{location.name}') as loc_cluster:
                loc_cluster.attr(label=location.name)

                # Recursively add clusters for child locations
                for child_loc in location.locations:
                    self._add_location_clusters(loc_cluster, child_loc)

                # Add component cluster if there are components
                if location.components:
                    with loc_cluster.subgraph(name=f'cluster_{location.name}_components') as comp_cluster:
                        comp_cluster.attr(style='dotted')
                        comp_cluster.attr(label='Components')
                        
                        # Calculate the number of rows needed for the components
                        num_rows = max(1, len(location.locations))
                        num_cols = 2
                        
                        # Add squares for each component, with invisible edges to order them in a column
                        for i, component in enumerate(location.components):
                            row = i // num_cols
                            col = i % num_cols
                            
                            comp_cluster.node(component.name, shape='box')
                            
                            if row > 0:
                                prev_comp = location.components[i - num_cols]
                                comp_cluster.edge(prev_comp.name + ':s', component.name + ':n', style='invis')
                            
                        # Add invisible edges to order components and locations in two columns
                        for i, child_loc in enumerate(location.locations):
                            row = i // num_cols
                            col = i % num_cols
                            
                            if col == 0:
                                prev_comp = location.components[-1] if location.components else None
                                prev_node = prev_comp.name + ':s' if prev_comp else location.name + ':n'
                                loc_cluster.edge(prev_node, child_loc.name + ':n', style='invis')
                            
                            else:
                                prev_loc = location.locations[i - 1]
                                loc_cluster.edge(prev_loc.name + ':s', child_loc.name + ':n', style='invis')
                            

        # If location has no child locations or components, represent as square
        else:
            parent_cluster.node(location.name, shape='box')






class LocationState(Enum):
    COHERENT = 'COHERENT'
    DEGRADATED = 'DEGRADATED'
    CRITICAL = 'CRITICAL'
    FAULT = 'FAULT'    
    UNINITIALIZED = 'UNINITIALIZED'
