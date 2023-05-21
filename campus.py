# from location import Location
from location import Location
from component import Component, ComponentType
from typing import Dict, Optional, cast
from warnings import warn
from copy import copy

from graphviz import Digraph

class Campus:
    def __init__(self) -> None:
        self.components: list[Component] = []
        self.locations: list[Location] = []

    def add_component(self, component: Component, type: ComponentType, location: Location):
        if not isinstance(component, Component):
            raise TypeError('Passed argument is not instance of Location') from None
        if not isinstance(type, ComponentType):
            raise TypeError('Passed argument \'type\' is not instance of ComponentType') from None
        if component in self.components:
            warn(f'Component {component.name} is being added twice to the same location')
        if Location not in self.locations:
            warn('Passed argument \'location_identifier\' not in added locations.\nAdded location.')
            self.add_location(location)
        
        copy_component: Component = copy(component)

        copy_component.type = type
        copy_component.location_identifier = location.location_identifier
        self.components.append(copy_component)

    def add_location(self, location: Location):
        if not isinstance(location, Location):
            raise TypeError('Passed argument is not instance of Location') from None
        if location in self.locations:
            return

        self.locations.append(location)

        for loc in location.locations:
            self.add_location(loc)




    def to_graph(self) -> Digraph:
        def generate_cluster(name: str, contents: Digraph) -> Digraph:
            cluster = Digraph(name=f'cluster_{name}')
            cluster.attr(label=name)
            cluster.subgraph(contents)
            return cluster

        def generate_component_graph(component: Component, parent_location_identifier: str) -> Digraph:
            graph = Digraph()
            component_identifier = f"{parent_location_identifier}_{component.name}"
            graph.node(component_identifier, label=component.name, shape='box')

            for sub_component in component.components:
                sub_component_identifier = f"{component_identifier}_{sub_component.name}"
                graph.node(sub_component_identifier, label=sub_component.name, shape='box')
                graph.edge(component_identifier, sub_component_identifier)

                graph.subgraph(generate_component_graph(sub_component, component_identifier))

            return graph

        def generate_location_graph(location: Location) -> Digraph:
            graph = Digraph()
            location_identifier = location.location_identifier
            subgraph = Digraph()
            subgraph.attr(rank='same')

            for sub_location in location.locations:
                subgraph.subgraph(generate_location_graph(sub_location))

            for component in self.components:
                if component.location_identifier == location_identifier:
                    component_identifier = f"{location_identifier}_{component.name}"
                    graph.node(component_identifier, label=component.name, shape='box')
                    subgraph.subgraph(generate_component_graph(component, location_identifier))
                    graph.edge(location_identifier, component_identifier)

            graph.subgraph(generate_cluster(location_identifier, subgraph))
            return graph

        graph = Digraph('G', format='png')
        graph.attr(overlap='false', splines='true', edge_attr={'arrowhead': 'none'})

        graph.subgraph(generate_location_graph(self.locations[0]))
        graph.subgraph(generate_component_graph(self.components[0], 'CampusCentral'))

        return graph