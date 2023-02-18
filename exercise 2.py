class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        weigth = 25
        tickness = 0.05
        intake = self.length * self.width * weigth * tickness / 1000
        print(f'Нужно {intake} тон асвальта')


road = Road(20000, 6)
road.intake()
print(road)
