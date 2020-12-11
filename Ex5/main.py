def task1():
    line = " "
    try:
        with open ("text_task1.txt", "a") as f_obj:
            while line != "":
                line = input()
                f_obj.write(line + "\n")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
def task2():
    my_f = open("text_task2.txt", "r")
    content = my_f.readlines()
    print(f"{len(content)} строк в файле.")

    for that_line in content:
        print(f"Строка №{content.index(that_line) + 1}: {len(that_line)}")
    my_f.close()
def task3():
    interim_map = {}
    end_map = {}
    sum_of_pay = 0
    try:
        with open("text_task3.txt", "r") as f_Name:
            desc_f = f_Name.readlines()
            print("Меньше 20 тыс. руб.:")
            for line in desc_f:
                partit_line = line.partition(' ')
                pay = float(partit_line[2])
                second_name = str(partit_line[0])
                interim_map = {second_name: pay} # Хачу славарь
                end_map.update(interim_map)
                if end_map.get(second_name) < 2*1e4:
                     print(f"{second_name}: {end_map.get(second_name)} руб.")
                sum_of_pay += end_map.get(second_name)
        sum_of_pay /= len(line)
        print(f"Средняя арифметическая зарплата у сотрудников: {sum_of_pay}")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
def task4():
    eng_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    my_in_f = open("text_task4_in.txt", "r")
    my_out_f = open("text_task4_out.txt", "w")
    content = my_in_f.readlines()
    for line in content:
        partit_line = line.partition(" — ")
        my_out_f.write(f"{eng_rus.get(partit_line[0])}{partit_line[1]}{str(partit_line[2])}")
    my_out_f.close()
    my_in_f.close()
def task5():
    sum = 0
    my_in_f = open("text_task5.txt", "w")
    my_in_f.write(input())
    my_in_f.close()
    my_in_f = open("text_task5.txt", "r")
    my_list = my_in_f.readline().split()
    my_in_f.close()
    for term in my_list:
        sum += int(term)
    print(sum)
def task6():
    interim_map = {}
    end_map = {}
    try:
        with open("text_task6.txt", "r") as f_Name:
            desc_f = f_Name.readlines()
            for line in desc_f:
                partit_line = line.partition(":") #разбиваем строку, получаем название предмета в [0]
                str = ""
                for part_part_line in partit_line[2]: #проходим по каждому символу строки
                    if ord(part_part_line) >= 48 and ord(part_part_line) <= 57: #если символ - цифра
                        str += part_part_line
                    if part_part_line == '(':
                        str += " " # сформировали строку состоящую только из чисел
                new_list = str.split() # получили список чисел по каждому предмету
                new_sum = 0
                for i in new_list:
                    new_sum += int(i) #сумма часов
                interim_map = {partit_line[0]: new_sum}
                end_map.update(interim_map) # сгенерировали словарь и добавили новые ключи и значения
            print(end_map)
    except IOError: #исключение
        print("Произошла ошибка ввода-вывода!")
def task7():
    all_firm = {}
    ooo_f = open("text_task7.txt", "w")
    ooo_f.write("firm_1   ООО   1000   5000\n"
                "firm_2   ОAО   12341   14321\n"
                "firm_3   UFO   10000   5555\n"
                "firm_4   ОAOAO   23412   10000\n"
                "firm_5   AUUF   10   1\n"
                "firm_6   ОoOoO  1   2\n")
    ooo_f.close()
    ooo_f = open("text_task7.txt", "r")
    content = ooo_f.readlines()
    profit_of_all_firms = 0
    for lines in content:
        lines = lines.split()
        profit = int(lines[-2]) - int(lines[-1])
        if profit > 0:
            that_firm = {lines[0]: "+" + str(profit)}
            all_firm.update(that_firm)
            profit_of_all_firms += profit
        else:
            that_firm = {lines[0]: "" + str(profit)}
            all_firm.update(that_firm)
    print(all_firm)
    print(f"Общая прибыль всех фирм - {profit_of_all_firms}")
    ooo_f.close()
# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
task7()