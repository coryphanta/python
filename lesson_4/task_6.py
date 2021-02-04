# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

# a)
index = 1
for num in count(int(input('Please enter start number '))):
    print(f"Value: {num}")
    if index % 11 == 0 and input("Continue? Press 'Y'").upper() != 'Y':
        print(f"Execution stopped")
        break
    index = index + 1

# b)
index = 1
initial_list = ["abc", 1, "e", 203, 0.34, -74]
for item in cycle(initial_list):
    print(f"Item: {item}")
    if index % 6 == 0 and input("Continue? Press 'Y'").upper() != 'Y':
        print(f"Execution stopped")
        break
    index = index + 1
