# Реализовать функцию int_func()
def int_func(string):
    # В программу должна попадать строка из слов,
    # разделенных пробелом.
    list_of_words = string.split(" ")
    list_capitalized_words = []
    for word in list_of_words:
        # принимающую слово из маленьких латинских букв
        formatted_word = word.lower()
        # возвращающую его же, но с прописной первой буквой.
        # Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
        capitalized_word = formatted_word.capitalize()
        list_capitalized_words.append(capitalized_word)
    return list_capitalized_words


def print_list_as_string(list_of_words):
    string_to_print = ' '.join(list_of_words)
    return string_to_print


input_string = input("Please enter any sentence or word ")
print(print_list_as_string(int_func(input_string)))
