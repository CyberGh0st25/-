def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")

def get_operation():
    while True:
        operation = input("Выберите операцию (+, -, *, /): ").strip()
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Ошибка: Введите корректную операцию.")

def calculate(num1, num2, operation):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."

def main():
    while True:
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")
        operation = get_operation()
        result = calculate(num1, num2, operation)
        print(f"Результат: {result}")

        repeat = input("Хотите выполнить еще одну операцию? (да/нет): ").strip().lower()
        if repeat != 'да':
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()