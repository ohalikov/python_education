e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

print("# 8.2  Вывести французский вариант слова walrus")
print(e2f["walrus"])
print()


print("# 8.3 Создать f2e на основе e2f")
f2e = {france_word: english_word for english_word, france_word in e2f.items()}
print(f2e)
print()

print("# 8.4 Вывести английский вариант слова chien из f2e")
print(f2e['chien'])
print()

print("# 8.5 Вывести множество английский слов из ключей e2f")
print(set(e2f))
print()

print('''
      Создайте многоуровневый словарь life . Используйте следующие строки для
ключей верхнего уровня: 'animals' , 'plants' и 'other' . Сделайте так, чтобы
ключ 'animals' ссылался на другой словарь, имеющий ключи 'cats' , 'octopi'
и 'emus' . Сделайте так, чтобы ключ 'cats' ссылался на список строк со значени-
ями 'Henri' , 'Grumpy' и 'Lucy' . Остальные ключи должны ссылаться на пустые
словари.
      ''')
cats_list_values = ['Henri', 'Grumpy', 'Lucy']
empty_dict = {}
dict_animals = {
    'cats': cats_list_values,
    'octopi': empty_dict,
    'emus': empty_dict
}

life = {
    'animals': dict_animals,
    'plants': empty_dict,
    'other': empty_dict
}

print("# 8.8 Выведите на экран ключи life['animals']")
print(life["animals"])
print()
print("# 8.9 Выведите значения life['animals']['cats']")
print(life["animals"]["cats"])

print('''
    8.10 Используйте генератор словаря, чтобы создать словарь squares . Используйте
    range(10), чтобы получить ключи. В качестве значений используйте возведен-
    ное в квадрат значение каждого ключа.
    ''')
squares = {key: key*key for key in range(10)}
print(squares)
print()
print('''
    8.11 Используйте генератор множества, чтобы создать множество odd из нечетных
чисел диапазона range(10) .
    ''')
xx = {x for x in range(10) if x % 2 == 1}
print(xx)

print('''
    8.12. Используйте включение генератора, чтобы вернуть строку 'Got ' и числа из
диапазона range(10) . Итерируйте по этой конструкции с помощью цикла for .
    ''')

str3 = [f'got {x}' for x in range(10)]
print(str3)

for thing in ('got %s' % number for number in range(10)):
    print(thing)

print()
print('''
      8.13
      Используйте функцию zip() , чтобы создать словарь из кортежа ключей
( 'optimist' , 'pessimist' , 'troll' ) и кортежа значений ( 'The glass is half full' ,
'The glass is half empty' , 'How did you get a glass? ’).
      ''')
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full',
          'The glass is half empty',
          'How did you get a glass'
          )

print(dict(zip(keys, values)))
print()

print(
    '''
    8.14 
        Используйте функцию zip() , чтобы создать словарь с именем movies , в котором
        объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a
        Plane'] и plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check
        your exits'] .
    '''
)

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster',
         'A haunted yarn shop', 'Check your exits']

movies = dict(zip(titles, plots))
print(movies)
