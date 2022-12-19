# sort и sorted

'''
    sort - функция, сортирующая сам список
    sorted - общая функция, которая возращает отсортированную копию списка.
'''

marxes_3 = ['Groucho', 'GummoВАФЫЫФВ', 'Chico00001203012030',
            'Bruno', 'Gummo', 'Harpo', 'Karl', 'Gummo', 'Gummo']


marxes_4 = ['Groucho', 'Gummo', 'Chico00001203012030',
            'Bruno', 'Gummo', 'Harpo', 'Karl', 'Gummo', 'Gummo']


marxes_3.sort()
sorted_marxes_4 = sorted(marxes_4)


print('marxes_3 =>', marxes_3)
print('\n\nsorted_marxes_4 =>', sorted_marxes_4)
