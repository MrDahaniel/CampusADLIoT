from __future__ import annotations
from typing import Optional
from sensor import Sensor
from graphviz import Digraph
from copy import copy

from enum import Enum

class Component:
    def __init__(self, name: str, location: Optional[str] = None) -> None:
        self.name: str = name
        self.location: Optional[str] = location
        self.components: list[Component] = []
        self.type: ComponentType
        self.state: ComponentState = ComponentState.UNINITIALIZED

    def add_component(self, component: Component) -> None:
        if not isinstance(component, Component):
            raise TypeError('Passed argument is not instance of Component')

        new_comp = copy(component)
        new_comp.location = None

        self.components.append(new_comp)

    def get_status(self) -> ComponentState:
        component_states = [comp.state for comp in self.components]
        
        if all(component_states):
            return ComponentState.OPTIMAL
        elif True in component_states:
            return ComponentState.DEGRADATED
        
        return ComponentState.FAULT

    def _add_component_nodes(self, dot: Digraph):
        self.node_name = f'{self.location}_{self.name}'
        dot.node(name=self.node_name, shape='box', label=self.name) # Self node
        dot.edge(self.node_name)

        


class ComponentType(Enum):
    MANDATORY = 'MANDATORY'
    OPTIONAL = 'OPTIONAL'

class ComponentState(Enum):
    OPTIMAL = 'OPTIMAL'
    DEGRADATED = 'DEGRADATED'
    FAULT = 'FAULT'
    UNINITIALIZED = 'UNINITIALIZED'


