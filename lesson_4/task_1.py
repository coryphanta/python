# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import payroll_script_tsk_1 as pr
from sys import argv

input_output_in_hours, input_rate_per_hour, input_bonus = argv

print("Salary is" + pr.calculate_salary(input_output_in_hours, input_rate_per_hour, input_bonus))
