# множество - это всего лишь НАБОР значений, а словарь содержит пары "ключ - значение"

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
print(drinks.items())  # список кортежей по 2 элемента.

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print(f"\n\nМы хотим выпить коктейль с водкой но не переносим лактозу")
# А вермут на вкус как керосин
print()
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)


print("\n\nМы хотим найти коктейль с апельсиновым соком или вермутом")
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
# ОПЕРАТОР ПЕРЕСЕЧЕНИЯ МНОЖЕСТВ &

print()
print("# Тоже самое что и в предыдущем примере")
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
