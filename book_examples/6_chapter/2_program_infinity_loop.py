# Бесконечный цикл пока не нажмешь q

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalizey())
