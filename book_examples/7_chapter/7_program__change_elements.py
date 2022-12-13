numbers = [1, 2, 3, 4]
numbers[1:3] = (93, 96, 32)
print(numbers)  # [1, 93, 96, 32, 4]

numbers[1:3] = 'wat?'
print(numbers)


# УДАЛЯЕМ заданный элемент с помощью оператора DEL
marxes = ['Groucho', 'Chico00001203012030', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])


del marxes[1]
print(marxes)

# Удаляем элемент по значению.
marxes_2 = ['Groucho', 'Chico00001203012030', 'Harpo', 'Gummo', 'Karl']
marxes_2.remove('Harpo')
print(marxes_2)

marxes_3 = ['Groucho', 'Gummo', 'Chico00001203012030',
            'Bruno', 'Harpo', 'Karl']

print(marxes_3.pop(1))


# Подсчитываем количество включений
marxes_4 = ['Groucho', 'Gummo', 'Chico00001203012030',
            'Bruno', 'Gummo', 'Harpo', 'Karl', 'Gummo', 'Gummo']
print('Gummo names -> count = ', marxes_4.count('Gummo'))


# Преобразуем список в строку
separator = ' * '
new_str_names = separator.join(marxes_4)
print(new_str_names)
