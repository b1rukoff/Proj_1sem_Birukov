# Вариант 2.
# Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг
# шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
p1 = input("Введите цену шоколадных конфет за кг: ")

while type(p1) != int:  # Обработка исключений для p1.
    try:
        p1 = int(p1)
    except ValueError:
        print("Неправильный ввод!")
        p1 = input("Введите цену шоколадных конфет за кг: ")
    if type(p1) == int and p1 < 0:
        print("Неправильный ввод!")
        p1 = input("Введите цену шоколадных конфет за кг: ")

s1 = input("Введите количество шоколадных конфет в кг: ")

while type(s1) != int:  # Обработка исключений для p1.
    try:
        s1 = int(s1)
    except ValueError:
        print("Неправильный ввод!")
        s1 = input("Введите количество шоколадных конфет в кг: ")
    if type(s1) == int and s1 < 0:
        print("Неправильный ввод!")
        s1 = input("Введите количество шоколадных конфет в кг: ")

p2 = input("Введите цену ирисок за кг: ")

while type(p2) != int:  # Обработка исключений для p2.
    try:
        p2 = int(p2)
    except ValueError:
        print("Неправильный ввод!")
        p2 = input("Введите цену ирисок за кг: ")
    if type(p2) == int and p2 < 0:
        print("Неправильный ввод!")
        p2 = input("Введите цену ирисок за кг: ")


s2 = input("Введите количество ирисок в кг: ")

while type(s2) != int:  # Обработка исключений для p1.
    try:
        s2 = int(s2)
    except ValueError:
        print("Неправильный ввод!")
        s2 = input("Введите количество ирисок в кг: ")
    if type(s2) == int and s2 < 0:
        print("Неправильный ввод!")
        s2 = input("Введите количество ирисок в кг: ")

print(f"Стоимость шоколадных конфет: {p1*s1} \nСтоимость ирисок: {p2*s2}"
      f"\nШоколадные конфеты дороже в {round((p1*s1) / (p2*s2), 1)} раз")
