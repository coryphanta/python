def calculate_sum(seq_for_calculation):
    sum_of_num = 0
    for num in seq_for_calculation:
        sum_of_num += int(num)
    return sum_of_num


def convert_str_to_lst(num_seq):
    return num_seq.split(" ")


def check_special_symbols_and_return_sum(seq_for_check):
    num_to_calculation = []
    result_with_code = {}
    for i in seq_for_check:
        try:
            number = int(i)
        except ValueError:
            # interrupt execution if not a number
            # If a special character is entered after several numbers,
            # then it needs to add the sum of these numbers to the previously received amount
            # and then complete the program.
            result_with_code[False] = calculate_sum(num_to_calculation)
            return result_with_code
        num_to_calculation.append(i)
        # If sequence contains only numbers then return sum of sequence
    result_with_code[True] = calculate_sum(num_to_calculation)
    return result_with_code


def parse_calculation_result(values_keys):
    value_iterator = iter(values_keys)
    return next(value_iterator)


sum_of_numbers = 0
global needs_execution
needs_execution = True
# The program requests the user for a space-separated string of numbers.
# The user can continue entering numbers until a special character is entered
# If a special character is entered instead of a number, the program ends.
while needs_execution:
    number_sequence = input("Please enter a sequence of numbers ")
    args = convert_str_to_lst(number_sequence)
    calculation_result = check_special_symbols_and_return_sum(args)
    # The sum of the newly entered numbers will be added to the already calculated amount.
    sum_of_numbers = sum_of_numbers + parse_calculation_result(calculation_result.values())
    needs_execution = parse_calculation_result(calculation_result.keys())
    # When the Enter button is pressed, the sum of the numbers should be displayed
    print("Sum is: " + str(sum_of_numbers))
