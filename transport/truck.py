from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color):
        super().__init__( capacity)
        self.color = color

    def __str__(self):
        return super().__str__() +f"Цвет грузовика: {self.color}"