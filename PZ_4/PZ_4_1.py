# Вариант 2.
# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и
# B (не включая числа A и B), а также количество N этих чисел.
N = 0
A = input("Введите число A: ")

while type(A) != int:  # Обработка исключений
    try:
        A = int(A)
    except ValueError:
        print("Неправильный ввод!")
        A = input("Введите число A: ")

B = input("Введите число B (должно быть больше числа A): ")

while type(B) != int:  # Обработка исключений
    try:
        B = int(B)
    except ValueError:
        print("Неправильный ввод!")
        B = input("Введите число B (должно быть больше числа A): ")
    if type(B) == int and B <= A:
        print("Неправильный ввод!")
        B = input("Введите число B (должно быть больше числа A): ")

while B > A and B - A > 1:
    print(B - 1)
    B -= 1
    N += 1
print("Количество чисел:", N)
