# 7.5
things = ["mozzarella", "cinderella", "salmonella"]

new_things = [x.capitalize() for x in things]
print(new_things)


# 7.6
new_things_2 = [x.upper() for x in things]
print(new_things_2)


# 7.8 - 7.9
# Вывести последний элемент с маленькой буквы
# и потом это слово наоборот и с большой буквы.
surprise = ["Groucho", "Chico", "Harpo"]
new_elem = surprise[-1].lower()
reverse_new_elem = new_elem[::-1]
print(new_elem)
print(reverse_new_elem.capitalize())

# 7.10
# Использовать списковое включение(генератор списков)
# Чтобы создать список even в котором будут содержаться четные числа
# в промежутке range(10)
even = [number for number in range(10) if number % 2 == 0]
print(even)


# 7.11
# Генератор рифм для прыжков через скакалку
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

# (first, second) в списке rhymes

start1_caps = " ".join([word.capitalize() + "!" for word in start1])

for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")
