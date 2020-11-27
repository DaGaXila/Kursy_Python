import script1
from random import randrange as rndrng
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    count = script1.fun_count(a, b, c)
    print(f"Зарплата = {count}")
def sort_for_2(a):
    b = []
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            b.append(a[i + 1])
    return b

def task2():
    a = []
    size = int(input("Введите размер списка:"))
    for i in range(size):
        a.append(rndrng(0, 100))
    print(a)
    print(sort_for_2(a))
def task3():
    print([s for s in range(20, 240, 1) if s % 20 == 0 or s % 21 ==0])
def task4():
    a = []
    b = []
    size = int(input("Введите размер списка:"))
    for i in range(size):
        a.append(rndrng(0, 200))
    for i in range(size):
        if a.count(a[i]) == 1:
            b.append(a[i])
    print(a)
    print(b)
from functools import reduce
def task5():
    items = []
    s = int(input("Cколько?)"))
    for i in range(0, s):
        items.append(rndrng(100, 1001, 2))
    mov_of_items = reduce(lambda x, y: x * y, items)
    print(items)
    print(mov_of_items)
    return
import script2
import script3
import itertools
def task6():
    my_list = script2.func_count(int(input("С какого числа?: ")), 1)
    print(my_list)
    script3.func_cycle(my_list, int(input("Сколько раз вывести?: ")))
def fact(n):
    c = 1
    for i in range(0, n):
        c *= i + 1
        print(f"{c} ")
        yield c
def task7():
    n = int(input("Сколько чисел? "))
    for el in fact(n):
        n
# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()