# Бесконечный цикл по не нажмеш q вычисляющий нечетный квадраты

while True:
    number = ''
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break

    try:
        number = int(value)
        if number % 2 == 0:
            continue
        print(number, "squared is", number*number)
    except Exception as e:
        print("INTEGER PLEASE, DALBOEB!!")
        continue
