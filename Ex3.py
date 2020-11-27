def func_dev(a, b):
    if b != 0:
        return a/b
    else:
        return False
def task1():
    dev_a_b = func_dev(6, 2)
    print(dev_a_b)
def print_func2(first_name, second_name, age, city, e_mail, phone):
    print(f"Имя - {first_name}, Фамилия - {second_name}, Год рождения - {age},"
          f" Город проживания - {city}, E-mail - {e_mail}, Телефон - {phone}")
    return
def task2():
    first_name = input()
    second_name = input()
    age = int(input())
    city = input()
    e_mail = input()
    phone = int(input())
    print_func2(first_name, second_name, age, city, e_mail, phone)
def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    else:
        return a + b
def task3():
    a, b, c = (int(input()) for _ in range(3))
    sum_of_bigger = my_func(a, b, c)
    print(sum_of_bigger)
def my_func4(x, y):
    mov = 1
    for _ in range(-y):
        mov *= x
    return 1/mov
def task4():
    x = float(input("x="))
    y = int(input("y="))
    while y >= 0:
        y = int(input("Try again."))
    print(my_func4(x, y))
def sum_func(a):
    sum_of = 0
    for i in a:
        sum_of += i
    print(f"Промежуточная сумма = {sum_of}")
    return sum_of


def task5():
    print("Символ - ! - окончить счёт.")
    sum_of = 0
    while 1:
        s = input("Введите числа через пробел:")
        c = s.find("!")
        s = s.partition(' ! ')
        a = list(map(int, s[0].split()))
        sum_of += sum_func(a)
        if c != -1:
            break
    print(f"Итоговая сумма = {sum_of}")
def int_func(my_string):
    return my_string.capitalize() + " "
def task6():
    f = ""
    my_string = input("Введите строку с маленькой буквы:")
    for i in my_string.split():
        f += int_func(i)
    print(f)

# task1()
# task2()
# task3()
# task4()
# task5()
task6()