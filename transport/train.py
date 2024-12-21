from .vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars):
        super().__init__( capacity)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return super().__str__() +f"Количество вагонов: {self.number_of_cars}"