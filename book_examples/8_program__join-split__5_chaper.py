import string

# Split - разделить
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
new_tasks_array = tasks.split(',')
print(new_tasks_array)

# strip/lstrip/rstrip - удалить пробелы и прочее
# удаление всех символов из последовательности
world = "      earth     "
new_word = world.strip()
print("БЕз пробелов -> ", new_word)

blurt = "What the...!!?,#"
print(blurt.strip('.?!'))
print(blurt.strip(string.punctuation))  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

prospector = "   What in tarnation ...??! !   "
print(prospector.strip(string.whitespace + string.punctuation))

# Join
strangers_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']

new_strangers_string = ', '.join(strangers_list)
another_way_to_join_strangers_list = '\n'.join(strangers_list)

print('\n', new_strangers_string, '\n')
print(another_way_to_join_strangers_list)

# Replace

setup = 'a famous duck goes into a famous bar...'
new_setup1 = setup.replace('a ', 'AB ', 100)  # заменяет все а с пробелом
new_setup2 = setup.replace('a', 'AB ', 100)  # заменяет все а
print(new_setup2)
'''
Иногда вам нужно убедиться в том, 
что подстрока является целым словом, началом слова и т. п.
'''
