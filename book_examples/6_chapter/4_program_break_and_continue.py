word = 'thud'

# Прерывание
for letter in word:
    if letter == 'x':
        print("EAK! An 'X'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

# range(начало, конец, шаг)
for x in range(10, -1, -2):
    print(x)

# list
print(list(range(2, -1, -1)))
