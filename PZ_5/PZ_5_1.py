# Вариант 2
# Составить функцию, которая напечатает сорок любых символов.
import random
import string


def generate(length):  # Функция, генерирующая случайные символы
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    if length == 1:
        print(length, "случайный символ:", rand_string)
    else:
        print(length, "случайных символов:", rand_string)


x = input("Введи количество символов, которое нужно сгенерировать (не больше 62): ")

while type(x) != int:  # Обработка исключений
    try:
        x = int(x)
    except ValueError:
        print("Неправильный ввод!")
        x = input("Введи количество символов, которое нужно сгенерировать (не больше 62): ")
    if type(x) == int and 0 >= x >= 63:
        print("Неправильный ввод!")
        x = input("Введи количество символов, которое нужно сгенерировать (не больше 62): ")

generate(x)
