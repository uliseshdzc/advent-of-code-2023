class Module:
    def __init__(self, type, state, destinations, memory = None) -> None:
        self.type = type
        self.state = state
        self.destinations = destinations
        self.memory = memory