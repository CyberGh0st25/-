def get_operation():
    while True:
        operation = input("Выберите операцию (+, -, *, /, **, sqrt): ").strip()
        if operation in ('+', '-', '*', '/', '**', 'sqrt'):
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
        elif operation == '**':
            return num1 ** num2
        elif operation == 'sqrt':
            return num1 ** 0.5
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно."