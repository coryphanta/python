def calculate_salary(output_in_hours, rate_per_hour, bonus):
    if not output_in_hours.isDigit() or not rate_per_hour.isDigit() or bonus.isDigit():
        raise Exception("Nononono! Bonus, Rate Per Hour and Output In Hours should be numbers")
    return (output_in_hours * rate_per_hour) + bonus
