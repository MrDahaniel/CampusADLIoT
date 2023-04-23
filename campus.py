from location import Location

class Campus:
    def __init__(self) -> None:
        self.locations: list[Location] = []

    def add_location(self, location: Location) -> None:
        if not isinstance(location, Location):
            raise TypeError('Passed argument is not instance of Location')
        self.locations.append(location)

    