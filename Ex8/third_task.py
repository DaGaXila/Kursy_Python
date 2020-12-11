class IntList:
    def __init__(self):
        self.my_list = []
    def in_el(self, i):
        try:
            self.my_list.append(int(i))
        except:
            try:
                self.my_list.append(float(i))
            except:
                print("Это не число!")
    def __str__(self):
        return f'Списко чисел: {self.my_list}'
if __name__ == "__main__":
    my_list = IntList()
    print("Вводите числа!")
    while 1:
        el_in = input()
        if el_in == "stop":
            print(my_list)
            break
        my_list.in_el(el_in)
