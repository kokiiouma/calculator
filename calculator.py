def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def powering(num_1, num_2):
    return num_1 ** num_2


def main():
    state = True
    while state:
        a = int(input("Введите число: "))
        b = int(input("Введите число: "))
        sign = input("Введите знак(+, -, *, /, **): ")

        if sign == "+":
            print(f'Результат: {addition(a, b)}')
        elif sign == "-":
            print(f'Результат: {subtraction(a, b)}')

        elif sign == "*":
            print(f'Результат: {multiplication(a, b)}')

        elif sign == "/":
            print(f'Результат: {division(a, b)}')

        elif sign == "**":
            print(f'Результат: {powering(a, b)}')

        else:
            print("Неизвестная команда.")

        answer = int(input("Продолжить? (1 - да, 0 - нет): "))

        if answer != 1:
            state = False


main()