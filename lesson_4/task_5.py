# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def multiplication(num1, num2):
    return num1 * num2


odd_list = [item for index, item in enumerate(range(100, 1001)) if item % 2 == 0]

result = reduce(multiplication, odd_list)

print(f"Odd list: {odd_list}")
print(f"Result of multiplication: {result}")
