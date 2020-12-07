from itertools import cycle
def func_cycle(list_of_num, rep):
    c = 0
    for el in cycle(list_of_num):
        if c > rep:
            break
        print(el)
        c += 1