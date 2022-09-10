# Создаём функцию калькулятор с аргументом expression и калькулятор должен вернуть результат
def calculator(expression):
    # переменная allowed – допустимый со значениями знаков, которые допустимы в вводе пользователем
    allowed = '+-/*'
    # условие "если нет ни одного(любого)(знака в выражения для знака в допустимых)
    if not any(sign in expression for sign in allowed):
        # то поднимаем ошибку значения (текст ошибки и допустимый словарь {allowed}
        # (f- ничего не меняет)f-строки - это пятый способ (sic!) форматирования строк в Python,
        # который очень похож на использование метода format().
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    # в цикле for перебераем знаки
    for sign in allowed:
        # Если знак есть в выражении
        if sign in expression:
            try:
                # условие, чтобы слева и справа были числа
                left, right = expression.split(sign)
                # условие, чтобы слева и справа были ЦЕЛЫЕ числа
                left, right = int(left), int(right)
                # если введённый знак равно плюс
                if sign == '+':
                    # то возвращаем программу в введённые числа со значением +,
                    # т.е числа у нас есть(выше для них условие) далее знак есть, проверяем чтобы всё совпадало
                    return left+right
                # если введённый знак равно минус
                elif sign == '-':
                    # то возвращаем программу в введённые числа со значением -, т.е условие к числам у нас уже прописаны выше
                    return left - right
                # если введённый знак равно умножить
                elif sign == '*':
                    # то возвращаем программу в введённые числа со значением *, т.е условие к числам у нас уже прописаны выше
                    return left * right
                    # если знак равно делить
                elif sign == '/':
                    # то возвращаем программу в введённые числа со значением /, т.е условие к числам у нас уже прописаны выше
                    return left / right
                    # исключения выдающие ошибку, например когда будет 2 знака или 1 число и т.д.
                    # TypeError это ошибка если будет введено не целое число
            except (ValueError, TypeError):
                # если будет введено не правильно(т.е не согласно тому условию, которое выше), то выскочит данная ошибка
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')
if __name__ == '__main__':
    print(calculator('25 * 5'))