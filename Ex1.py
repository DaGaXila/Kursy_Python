def task1():
    var_int = 5
    var_float = var_int + 7.3
    print(var_int, var_float)
    var_int = int(input("Введите целое число:"))
    var_str = input("Введите строку:")
    print(var_int, var_str)
def task2():
    time = int(input("Введите время в секнудах:"))
    hours = time / 3600
    minutes = time / 60 % 60
    seconds = time % 60
    if hours < 10:
        hours = "0%d:" % hours
    else:
        hours = "%d:" % hours
    if minutes < 10:
        minutes = "0%d:" % minutes
    else:
        minutes = "%d:" % minutes
    if seconds < 10:
        seconds = "0%d" % seconds
    else:
        seconds = "%d" % seconds
    total_time = print(hours + minutes + seconds)
def task3():
    n = int(input("Введите число:"))
    super_n = str(n) * 2
    double_super_n = str(n) * 3
    mega_super_n = int(n) + int(super_n) + int(double_super_n)
    print(mega_super_n)
def task4():
    n_input = int(input("Введите целое положительное число:"))
    n_mem = n_input
    start_max = 0
    i = 0
    while n_mem > 1:
        i += 1
        if n_mem % 10 > start_max:
            start_max = n_mem % 10
        n_mem /= 10
    print("Максимальная цифра в числе %d - это %d" % (n_input, start_max))
def task5():
    revenue = int(input("Введите сумму выручки фирмы:"))
    costs = int(input("Введите сумму издержки фирмы:"))
    if revenue > costs:
        print("Фирма работает на прибыль")
        rent = (revenue - costs) / revenue
        print("Рентабельность фирмы - %.4f %%" % (rent * 100))
        amo_emp = int(input("Введите количество сотрудников:"))
        print("Значение прибыли фирмы к одному сотруднику - %.3f" % (revenue / amo_emp))
    else:
        print("Фирма работает на убыль")
def task6():
    start_km = int(input("Введите начальную дистанцию, км:"))
    record_km = int(input("Введите желаемый результат спортсмена, км:"))
    day_i = 0
    while start_km < record_km:
        start_km *= 1.1
        day_i += 1
    print("Желаемый результат будет достигнут на %d день! В жизни не применимо. Задача - ложь." % day_i)

# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
