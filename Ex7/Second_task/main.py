from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, _name, _param):
        self._name = _name
        self._param = _param
    @property
    def get_value_material(self):
        return
    @property
    def output(self):
        return

    def __add__(self, other):
        return self.get_value_material + other.get_value_material
    def output_sum(self):
        return

class Coat(Clothes):
    @property
    def get_value_material(self):
        return self._param / 6.5 + 0.5
    def output(self):
        return f'Для {self._name} нужно {self._param / 6.5 + 0.5} м ткани'
class Costume(Clothes):
    @property
    def get_value_material(self):
        return 2 * self._param + 0.3
    def output(self):
        return f'Для {self._name} нужно {2 * self._param + 0.3} м ткани'

if __name__ == "__main__":
    sum_of_clothes = 0
    coat = Coat("Пальто", 400)
    costume = Costume("Костюм", 55)
    coat1 = Coat("Новое пальто", 300)
    costume1 = Costume("Новый костюм", 200)
    print(coat.output())
    print(costume.output())
    sum_of_clothes += coat + costume
    # print(sum_of_clothes)
    sum_of_clothes += coat1 + costume1
    print(f"Ткани нужно {sum_of_clothes}")

