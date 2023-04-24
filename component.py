from __future__ import annotations
from sensor import Sensor

from enum import Enum

class Component:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sensors: list[Sensor] = []
        self.type: ComponentType
        self.state: ComponentState = ComponentState.UNINITIALIZED

    def add_sensor(self, sensor: Sensor) -> None:
        if not isinstance(sensor, Sensor):
            raise TypeError('Passed argument is not instance of Sensor')
        self.sensors.append(sensor)

    def get_status(self) -> ComponentState:
        sensor_states = [sens.state for sens in self.sensors]
        
        if all(sensor_states):
            return ComponentState.OPTIMAL
        elif True in sensor_states:
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
