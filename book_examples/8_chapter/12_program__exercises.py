'''
    Во всех случаях, за исключением множеств, мы ПОЛУЧАЕМ ДОСТУП  к отдельному элементу
    с помощью квадртаных скобок. 
    
    Для списка и кортежа значение, находящееся в квадратных скобках является целочисленным смещением/
    Для словаря же оно является ключом. 
    Везде результатом будем зззначение. для множества: значение либо есть, либо нет. Ключей и индексов нет.
    

'''

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {
    'Groucho': 'banjo',
    'Chico': 'piano',
    'Harpo': 'harp'
}
marx_set = {
    'Groucho',
    'Chico',
    'Harpo'
}

print(marx_list[2])  # Harpo
print(marx_tuple[2])  # Harpo
print(marx_dict['Harpo'])

print('Harpo' in marx_dict)
