class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        __income = {'profit': self.profit, 'bonus': self.bonus}
        return __income


manager = Position('Petr', 'Petrov', 'manager', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())
