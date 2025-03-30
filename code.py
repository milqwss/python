# 1. Форматирование строк

name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

# Метод format
formatted_string_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
print("Реализация через format:")
print(formatted_string_format)

# f-string
formatted_string_fstring = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print("\nРеализация через f-string:")
print(formatted_string_fstring)


# 2. Четность числа

while True:
    try:
        number = int(input("Введите число: "))
        if number <= 0:
            print("Ошибка: введите положительное целое число.")
        elif number % 2 == 0:
            print(f"Число {number} является четным")
        else:
            print(f"Число {number} не является четным")
        break  # Выходим из цикла, если ввод корректен
    except ValueError:
        print("Ошибка: введено не число")



# 3. Проверка возраста

while True:
    try:
        age = int(input("Введите ваш возраст: "))
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
        elif age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")
        break
    except ValueError:
        print("Ошибка: введено не число!")


# 4. Длина числа

while True:
    user_input = input("Введите число (или 'exit' для выхода): ")
    if user_input.lower() == "exit":
        print("Выход из программы...")
        break
    try:
        num = int(user_input)
        if user_input.lstrip('-').isdigit(): # Проверка на цифры выполняется для строки user_input
            print(f"В этом числе {len(str(num))} цифр.") # Преобразование в строку внутри print
        else:
            print("Ошибка: данные не являются числом.")
    except ValueError:
        print("Ошибка: данные не являются числом.")
