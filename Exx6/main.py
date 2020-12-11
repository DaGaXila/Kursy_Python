import time as t
class TrafficLight:
    color = ["red", "yellow", "green"]
    def running(self, rep):
        print("Врубаем светофор")
        for _ in range(0, rep):
            print(TrafficLight.color[0])
            t.sleep(7)
            print(TrafficLight.color[1])
            t.sleep(2)
            print(TrafficLight.color[2])
            t.sleep(6)
def task_one():
    traffic_light = TrafficLight()
    traffic_light.running(2)
class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
    def _calculation(self, mass, fat):
        return self.length * self.width * mass * fat
def task_two():
    my_road = Road(5600, 20)
    print(f"Потребуется {my_road._calculation(50, 2)} тонн асфальта")
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")
def task_three():
    first_man = Position("Danila", "Gazov", "Smoker", 1000, 500)
    print(f"{first_man.get_full_name()} получает {first_man.get_total_income()} денег")
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"{self.name}, поехали!")
    def stop(self):
        self.speed = 0
        print("АСТАНАВИТЭСЬ!")
    def turn(self, direction):
        trans_direction = {0: "лево", 1: "право"}
        print(f"{self.name} повернул на{trans_direction.get(int(direction))}")
    def show_speed(self):
        print(f"Скорость - {self.speed}")
class TownCar(Car):
    def show_speed(self):
            if self.speed > 60:
                print(f"Ваша скорость, {self.name}, - {self.speed}, вы превышаете на {self.speed - 60}")
            else:
                print(f"Ваша скорость, {self.name}, - {self.speed}")
            return self.speed
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Ваша скорость, {self.name}, - {self.speed}, вы превышаете на {self.speed - 40}")
        else:
            print(f"Ваша скорость, {self.name}, - {self.speed}")
        return self.speed
class SportCar(Car):
    def press_gas(self):
        self.speed += 10
        print(f"Газу!")
        return self.speed
    def get_speed(self):
        return self.speed
    def show_speed(self):
        print(f"Ваша скорость, {self.name}, - {self.speed}")
class PoliceCar(Car):
    def police_func(self, _pursuit):
        if self.is_police == False:
            print(f"{self.name}, вы не полицейский. Выйдете из машины!")
            return False
        self.pursuit = _pursuit
        if self.pursuit == True:
            self.speed += 1
            return self.speed
    def stop(self):
        print("Миссия выполнена!")
        self.speed = 0
    def get_speed(self):
        return self.speed
def task_four():
    town_car = TownCar(70, "red", "Misha", False)
    work_car = WorkCar(40, "green", "Fedya", False)
    sport_car = SportCar(100, "black", "Danila", False)
    police_car = PoliceCar(80, "blue", "Musor", True)
    town_car.show_speed()
    work_car.show_speed()
    sport_car.go()
    sport_car.press_gas()
    sport_car.press_gas()
    if police_car.police_func(False) == False:
        return 0
    if sport_car.get_speed() > 110:
        print("По коням!")
        police_car.go()
        while sport_car.get_speed() >= police_car.get_speed():
            police_car.police_func(True)
        for i in range(0, 2):
            # 0 или 1
            turn_of = input("ПОВОРАЧИВАЙ!\n")
            sport_car.turn(turn_of)
            police_car.turn(turn_of)
        sport_car.stop()
        police_car.stop()
        sport_car.show_speed()
        print("Нарушитель пойман!")
        police_car_but = PoliceCar(80, "blue", "Danila", False)
        police_car_but.police_func(False)
class Stationary:
    def __init__(self, title):
        self._title = title
    def draw(self):
        print("Запуск отрисовки")
        return 0
class Pen(Stationary):
    def draw(self):
        print(f"Картина '{self._title}'. Рисую ручкой!")
        return 1
class Pencil(Stationary):
    def draw(self):
        print(f"Картина '{self._title}'. Рисую карандашом!")
        return 2
class Handle(Stationary):
    def draw(self):
        print(f"Картина '{self._title}'. Рисую маркером!")
def task_five():
    pen = Pen("Тьма")
    pencil = Pencil("Дырка")
    handle = Handle("Жирность")
    pen.draw()
    pencil.draw()
    handle.draw()

# task_one()
# task_two()
# task_three()
# task_four()
task_five()