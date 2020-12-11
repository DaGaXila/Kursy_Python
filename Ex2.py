def task1():
    my_second_list = [1, 2, 3]
    my_list = ["how", "are", "you", "Im", 9, "Thank u", my_second_list]
    i = 0
    while len(my_list) > i:
        print(type(my_list[i]))
        i += 1

def task2():
    #n = int(input("Количество элементов:"))
    i = 0
    my_list = []
    while 1:
        my_list.append(input())

        if my_list[i] == "[]":
            break
        if (i % 2) != 0:
            s = my_list[i - 1]
            my_list[i - 1] = my_list[i]
            my_list[i] = s
        print(my_list)
        i += 1
    my_list.pop(-1)
    print(my_list)

def task3_0():
    my_dict = {1: "Jan", 2: "Feb", 3: "Mart", 4: "April", 5: "May", 6: "June",
               7: "July", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
    numb = int(input("Введите номер месяца:"))
    print(my_dict.get(numb))
def task3_1():
    list_of_month = ["Jan", "Feb", "Mart", "April", "May", "June",
               "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    n = int(input("Введите номер месяца:"))
    print(list_of_month[n - 1])
def task4():
    my_str = str(input("Введите строку:"))
    my_str = my_str.split(" ")
    i = 0
    for words in my_str:
        print("%d: %s" % (i, my_str[i]))
        i += 1
def task5():
    print("Рейтинг!")
    my_list = [1, 10, 3, 0, 100, 2]
    while 1:
        choose = input("Внести новые данные? y/n:")
        if choose == "y":
            my_list.append(int(input()))
        if choose == "n":
            break
        my_list.sort()
    my_list.reverse()
    print(my_list)
def task5_0():
    print("Рейтинг!")
    my_list = [1, 10, 3, 0, 100, 2]
    my_list.sort()
    my_list.reverse()
    while 1:
        choose = input("Внести новые данные? y/n:")
        if choose == "y":
            my_list.append(int(input()))
        if choose == "n":
            break
    sort_task5_0(my_list)
    print(my_list)
def sort_task5_0(a):
    for wow in a:
        i = 0
        while i < len(a) - 1:
            if a[i] < a[i + 1]:
                f = a[i]
                a[i] = a[i + 1]
                a[i + 1] = f
            i += 1
from array import array
def task6():
    list_of_tuple = []
    tuple_of_dict = tuple()
    dict_of = {}
    i = 0
    while 1:
        i += 1
        choose = input("Внести новые данные? y/n:")
        if choose == "y":
            dict_of[i] = {"Название": input(), "Цена": input(),
                               "Количество": input(), "Единица": input()}
            tuple_of_dict = (i, dict_of[i])
            list_of_tuple.append(tuple_of_dict)
        if choose == "n":
            break
    print(list_of_tuple)
    j = 1
    k = 1
    total_list = []
    new_list = []
    help_dict = {1: "Название", 2: "Цена", 3: "Количество", 4: "Единица"}
    while k < 5:
        while j < i:
            new_list.append(dict_of[j].get(help_dict.get(k)))
            j += 1
        new_new_list = new_list.copy()
        j = 1
        new_dict = {help_dict.get(k): new_new_list}
        k += 1
        new_list.clear()
        total_list.append(new_dict)
    print(total_list)
#task1()
# task2()
# task3_0()
# task3_1()
# task4()
# task5()
# task5_0()
task6() #Если только этот код будет проверять препод, рассказываю. Тупо вышло, что я сделал список словарей со списками по каждому ключу.
# Инвалидно и велосипедно. Но переделывать не буду. Очень многому научился в ходе решения 6 задачи