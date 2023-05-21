from __future__ import annotations
from typing import cast
from sensor import Sensor
from graphviz import Digraph
from copy import copy

from enum import Enum

class Component:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.components: list[Component] = []
        self.location_identifier: str | None = None
        self.type: ComponentType
        self.state: ComponentState = ComponentState.UNINITIALIZED

    def add_component(self, component: Component) -> None:
        if not isinstance(component, Component):
            raise TypeError('Passed argument is not instance of Component')

        new_comp = copy(component)

        self.components.append(new_comp)

    def get_status(self) -> ComponentState:
        component_states = [comp.state for comp in self.components]
        
        if all(component_states):
            return ComponentState.OPTIMAL
        elif True in component_states:
            return ComponentState.DEGRADATED
        
        return ComponentState.FAULT


        

        


class ComponentType(Enum):
    MANDATORY = 'MANDATORY'
    OPTIONAL = 'OPTIONAL'

class ComponentState(Enum):
    OPTIMAL = 'OPTIMAL'
    DEGRADATED = 'DEGRADATED'
    FAULT = 'FAULT'
    UNINITIALIZED = 'UNINITIALIZED'


