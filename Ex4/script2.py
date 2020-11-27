from itertools import count
from math import sqrt as sq
def func_count(start, step):
    m = start
    my_list = []
    i = 0
    for el in count(start):
        i += 1
        if i > sq(el):
            break
        else:
            my_list.append(el)
            print(el)
    return my_list