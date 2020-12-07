class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сложили {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Вычли {sub}' if sub > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return f'Разделили {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Умножили {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result

if __name__ == "__main__":
    cell = Cell(24)
    cell_2 = Cell(2)
    print(cell + cell_2)
    print(cell - cell_2)
    print(cell / cell_2)
    print(cell * cell_2)
    print(cell.make_order(10))