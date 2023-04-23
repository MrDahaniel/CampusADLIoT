from sensor import Sensor

class Component:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sensors: list[Sensor] = []

    def add_sensor(self, sensor: Sensor) -> None:
        if not isinstance(sensor, Sensor):
            raise TypeError('Passed argument is not instance of Sensor')
        self.sensors.append(sensor)


