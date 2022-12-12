def printable_tuple(my_tuple):
    print(type(my_tuple))


empty_tuple = 'Groucho', 'dsfdasasdffa',
print('===================\n',
      type(empty_tuple)
      )
print(empty_tuple, '\n===================')

# Передача tuple, как аргумента функции.
one_marx = ('Groucho',)
printable_tuple(('Groucho',))  # так tuple
print(type(('Grouncho',)))  # вот так tuple
print(type('Grouncho',), '\n===================')  # str
