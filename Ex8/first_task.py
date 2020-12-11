class Date:
    def __init__(self, start_str):
        Date.start_str = start_str
    @classmethod
    def translate_date(cls):
        list_of_date = []
        month = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
                 "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
        partit_str = list(map(str, cls.start_str.split("-")))
        list_of_date.append(int(partit_str[0]))
        if month.get(partit_str[1]) == None:
            list_of_date.append(int(partit_str[1]))
        else:
            list_of_date.append((month.get(partit_str[1])))
        list_of_date.append(int(partit_str[2]))
        if Date.valid_date(list_of_date) == 0:
            Date.list_of_date = list_of_date
            return list_of_date
    @classmethod
    def __str__(cls):
        try:
            if cls.list_of_date[1] < 10:
                cls.list_of_date[1] = '0' + str(cls.list_of_date[1])
            if cls.list_of_date[0] < 10:
                cls.list_of_date[0] = '0' + str(cls.list_of_date[0])
            return f'{cls.list_of_date[0]}.{cls.list_of_date[1]}.{cls.list_of_date[2]}'
        except:
            return "Ошибка входных данных"
    @staticmethod
    def valid_of_count(count, month):
        if month == 1 or month == 3 or month == 7 or month == 8 or month == 10 or month == 12 and count <= 31:
            return 0
        if month == 4 or month == 5 or month == 6 or month == 9 or month == 11 and count <= 30:
            return 0
        if month == 2 and count <= 28:
            return 0
        return 1
    @staticmethod
    def valid_date(list_of_date):
        if Date.valid_of_count(list_of_date[0], list_of_date[1]) == 0:
            if list_of_date[1] > 0 and list_of_date[1] < 12:
                if list_of_date[2] <= 2020:
                    print("Date is ok")
                    return 0
                else:
                    print("Age is not ok")
                    return 3
            else:
                print("Month is not ok")
                return 2
        else:
            print("Count is not ok")
            return 1
if __name__ == "__main__":
    first = Date("28-february-1980")
    Date.translate_date()
    print(first)
    second = Date("30-3-90")
    Date.translate_date()
    print(second)
    third = Date("31-11-2020")
    Date.translate_date()
    print(third)