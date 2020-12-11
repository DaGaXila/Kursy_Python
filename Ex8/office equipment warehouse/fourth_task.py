from collections import Counter
class Warehouse:
    money = 0
    def __init__(self, series_and_number, color, purchase_price, market_price):
        self.series_and_number = series_and_number
        self.color = color
        self.purchase_price = purchase_price
        self.market_price = market_price
        Warehouse.money -= int(self.purchase_price)
    @property
    def count(self):
        return
    @classmethod
    def my_money(cls):
        print(f'Ваш кредит {Warehouse.money}')
class Printer(Warehouse):
    __printers = []
    def __init__(self, series_and_number, color, purchase_price, market_price, one, two, three):
        self.parametres = [one, two, three]
        super().__init__(series_and_number, color, purchase_price, market_price)
        Printer.__printers.append(self)
    @classmethod
    def count(cls):
        return print(f'{len(cls.__printers)}')
    def delete(self, index):
        Warehouse.money += int(self.market_price)
        print(Printer.__printers.pop(index))
        del self
    def __str__(self):
        return f'Имя - {self.series_and_number}; уникальные параметр предмета:{self.parametres}'
class Scanner(Warehouse):
    __scanners = []
    def __init__(self, series_and_number, color, purchase_price, market_price, one):
        self.parametres = [one]
        super().__init__(series_and_number, color, purchase_price, market_price)
        Scanner.__scanners.append(self)
    @classmethod
    def count(cls):
        return print(f'{len(cls.__scanners)}')
    def delete(self, index):
        Warehouse.money += int(self.market_price)
        Scanner.__scanners.pop(index)
        return self
    def __str__(self):
        return f'Имя - {self.series_and_number}; уникальные параметр предмета:{self.parametres}'
class Copier(Warehouse):
    __copiers = []
    def __init__(self, series_and_number, color, purchase_price, market_price, one, two):
        self.parametres = [one, two]
        super().__init__(series_and_number, color, purchase_price, market_price)
        Copier.__copiers.append(self)
    @classmethod
    def count(cls):
        return print(f'{len(cls.__copiers)}')
    def delete(self, index):
        Warehouse.money += int(self.market_price)
        Copier.__copiers.pop(index)
        return self
    def __str__(self):
        return f'Имя - {self.series_and_number}; уникальные параметр предмета:{self.parametres}'
#Функция выбора покупателем товара
def select_eq():
    choose = input("scanner/printer/copier\n")
    if choose == "copier":
        print("Коперы:")
        for x in range(len(list_of_copier)):
            print(list_of_copier[x])
        i = int(input("Укажите пальцем... (0, 1, ... 10)"))
        list_of_copier[i].delete(i)
        del list_of_copier[i]
    if choose == "scanner":
        print("Cканеры:")
        for x in range(len(list_of_scanner)):
            print(list_of_scanner[x])
        i = int(input("Укажите пальцем... (0, 1, ... 10)"))
        list_of_scanner[i].delete(i)
        del list_of_scanner[i]
    if choose == "printer":
        print("Принтеры:")
        for x in range(len(list_of_printer)):
            print(list_of_printer[x])
        i = int(input("Укажите пальцем... (0, 1, ... 10)"))
        list_of_printer[i].delete(i)
        del list_of_printer[i]
#Очередная инвалидная костыльная функция
def my_except(new_data):
    while type(new_data[2]) != float and type(new_data[2]) != int:
        new_data[2] = float(input("Введите цену!!"))
    while type(new_data[3]) != float  and type(new_data[3]) != int:
        new_data[3] = float(input("Введите цену!"))
    return new_data[2], new_data[3]
#Функция добавления объекта на склад
def add_eq():
    choose = input("scanner/printer/copier\n")
    new_data = []
    if choose == "scanner":
        print("Введите: серию и номер\t цвет \t закупочную цену\t рыночную цену \t 1-ый параметр")
        for i in range(5):
            new_data.append(input())
        new_data[2], new_data[3] = my_except(new_data)
        list_of_scanner.append(Scanner(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4]))
        print("Сканнер добавлен!")
    if choose == "printer":
        print("Введите: серию и номер\t цвет \t закупочную цену\t рыночную цену \t 1-ый параметр\t 2-ой параметр \t 3-ий параметр")
        for i in range(7):
            new_data.append(input())
        new_data[2], new_data[3] = my_except(new_data)
        list_of_printer.append(Printer(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5], new_data[6]))
        print("Принтер добавлен!")
    if choose == "copier":
        print("Введите: серию и номер\t цвет \t закупочную цену\t рыночную цену \t 1-ый параметр \t 2-ой параметр")
        for i in range(6):
            new_data.append(input())
        new_data[2], new_data[3] = my_except(new_data)
        list_of_copier.append(Copier(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5]))
        print("Копиер добавлен!")
#Функция вывода на экран всех объектов
def print_all_eq():
    print("Принтеры:")
    for x in range(len(list_of_printer)):
        print(list_of_printer[x])
    print("Коперы:")
    for x in range(len(list_of_copier)):
        print(list_of_copier[x])
    print("Cканеры:")
    for x in range(len(list_of_scanner)):
        print(list_of_scanner[x])
#Функция вывода на экран финансов
def get_money():
    Warehouse.my_money()
list_of_printer = []
list_of_scanner = []
list_of_copier = []
#Меню
def menu(selected):
    if selected == "add":
        add_eq()
    if selected == "output":
        print_all_eq()
    if selected == "money":
        get_money()
    if selected == "buy":
        select_eq()
if __name__ == "__main__":
    with open("input.txt", "r") as input_txt:
        content = input_txt.readlines()
    input_txt.close()
    list_of_list = []
    for line in content:
        list_of_list.append(list(map(str, line.split())))
    print(list_of_list)
    for i in list_of_list:
        try:
            list_of_printer.append(Printer(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        except:
            try:
                list_of_copier.append(Copier(i[0], i[1], i[2], i[3], i[4], i[5]))
            except:
                list_of_scanner.append(Scanner(i[0], i[1], i[2], i[3], i[4]))
    #
    while(1):
        print("add/output/buy/money/exit")
        menu(input())
    #
