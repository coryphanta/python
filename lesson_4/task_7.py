# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(last_number):
    result = 1
    for num in range(1, last_number + 1):
        result = result * num
        yield result


index = 1
last_number = int(input("Please enter the last number "))
for el in fact(last_number):
    if index > last_number:
        break
    print(f"Element: {el}")
