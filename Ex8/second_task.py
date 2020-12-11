class ErrorNull(Exception):
    def dev_null(self, numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return f'Ошибка деления на ноль'
if __name__ == "__main__":
    div = ErrorNull()
    print(div.dev_null(5, 0))
    print(div.dev_null(6, 2))
