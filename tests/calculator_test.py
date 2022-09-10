# Прописываем необходимые(стандартные) импорты. Данные импорты автоматически прописываются
# если при создании этого python файла выбрать расширение unit test
from unittest import TestCase, main
# Прописываем импорт из папки и название функции, для которой будут писаться тесты.
from calculator import calculator


# создаём класс CalculatorTest. Он наследуется от TestCase(т.е в скобках пишется от чего наследуется класс.
# TestCase - это библиотека которую импортировали выше
class CalculatorTest(TestCase):
    # начинаем с "позитивных" тестов, т.е с тестов, где всё будет хорошо и правильно введено и правильный ответ будет
    # создаём функцию(тест) test_plus(название должно быть логичным, т.е тестируем знак плюс)
    def test_plus(self):
        # прописываем условие с участием assert.  assertEqual - это специальный метод для тестов
        self.assertEqual(calculator('2+2'), 4)
    # далее прописываем аналогичные позитивные тесты для других знаков
    def test_minus(self):
        self.assertEqual(calculator('5-2'), 3)
    def test_multiply(self):
        self.assertEqual(calculator('8*2'), 16)
    def test_division(self):
        self.assertEqual(calculator('9/3'), 3)

    # создаём функцию (тест) если нет знака
    def test_no_signs(self):
        # (with self контекстный менеджер)  assertRaises(убедись, что падает исключение)
        # ValueError - тип исключения(т.е кокое исключение),  as e это мы получили само исключение
        with self.assertRaises(ValueError) as e:
            # вызываем функцию, которая и должна это исключение вызвать
            calculator('dfdfdf')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    # создаём функцию (тест) если два одинаковых знака или другие не верно введённые знаки
    def test_numbers(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2b+')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    # создаём функцию (тест) если введены не целые числа
    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2,2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    # создаём функцию (тест) для строк, т.е знак какой то есть и он должен соединять какие буквы
    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+a')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()