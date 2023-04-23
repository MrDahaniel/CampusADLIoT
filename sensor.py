class Sensor:
    def __init__(self, name: str) -> None:
        self.name: str = name  
        self.state: bool = False

    def update_state(self, input):
        if not input is None:
            self.state = True
        else:
            self.state = False