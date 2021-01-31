# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Implement a function that takes multiple parameters:
# name, surname, year of birth, city of residence, email, phone.
# The function should take parameters as named arguments.
def print_personal_info(name, surname, year_of_birth, city, email, phone):
    print("name: " + name + " surname: " + surname + " year of birth: " + year_of_birth
          + " city of residence: " + city + " email: " + email + " phone: " + phone)


inputName = input("Please enter your name")
inputSurname = input("Please enter your surname")
inputYear = input("Please enter your year of birth")
inputCity = input("Please enter your city of residence")
inputEmail = input("Please enter your email")
inputPhone = input("Please enter your phone")

# Implement the output of user data in one line.
print(print_personal_info(inputName, inputSurname, inputYear, inputCity, inputEmail, inputPhone))
