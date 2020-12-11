from random import randrange as rndrng
#На вход подаётся не матрица, а список значений
class Matrix:
    def __init__(self, list_of_values, _volume_columns, _volume_rows):
        self._list_of_values = list_of_values
        self._volume_columns = _volume_columns
        self._volume_rows = _volume_rows
        Matrix.forming_matrix(self)
    def forming_matrix(self):
        self._list_M = []
        self._list_of_list_M = []
        _copy_of_list_M = []
        k = 0
        for i in range(0, self._volume_rows):
            for j in range(0, self._volume_columns):
                if k < len(self._list_of_values):
                    self._list_M.append(self._list_of_values[k])
                    k += 1
                else:
                    self._list_M.append(0)
            self._list_of_list_M.append(self._list_M.copy())
            self._list_M.clear()
        return self._list_of_list_M
    def __str__(self):
        self.new_string = "["
        for i in self._list_of_list_M:
            self.new_string += f"\n{i}"
        self.new_string += "\n]"
        return self.new_string
    def __add__(self, other):
        sum_of_M = []
        for i1, i2, i in zip(self._list_of_list_M, other._list_of_list_M, range(0, self._volume_rows)):
            for j1, j2 in zip(self._list_of_list_M[i], other._list_of_list_M[i]):
                    sum_of_M.append(j1 + j2)
        return Matrix(sum_of_M, self._volume_columns, self._volume_rows)

if __name__ == "__main__":
    my_list = []
    x = int(input("Количество строк: "))
    y = int(input("Количество столбцов: "))
    for _ in range(100):
        my_list.append(rndrng(0, 20))
    first_M = Matrix(my_list, x, y)
    print(first_M)
    my_list = []
    for _ in range(100):
        my_list.append(rndrng(0, 20))
    second_M = Matrix(my_list, x, y)
    print(second_M)
    third_M = first_M + second_M
    print(f"Сумма матриц: \n{third_M}")
