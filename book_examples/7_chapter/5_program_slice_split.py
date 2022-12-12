# Создаем список или преобразуем в список с помощью функции list()

another_empty_list = list()
print(another_empty_list)

print(list('cat'))  # также с помощью функции list можно преобразовать tuple -> list

talk_like_a_pirate_day = '9/19/2019'
result_of_split_day = talk_like_a_pirate_day.split('/')  # ['9', '19', '2019']
print(result_of_split_day)


# Get element throw construction offset: var[-1]
marxes = ['Grouncho', 'Chico', 'Harpo']
print(marxes[-3])  # this is max offset, 'cause -4 will be type error


# Get element thow construction slice: var[::2]
# получить нечетны элемент
print(marxes[::2])
print(marxes[::-1])

'''
    Все что выше не затрагивало исходный массив
'''
marxes_2 = ['Grouncho', 'Chico', 'Harpo']
print(f'marxes_2 -> {marxes_2}')

marxes_2_start_offset = 2
marxes_2_end_offset = 3
print(f'marxes_2[{marxes_2_start_offset}:{marxes_2_end_offset}] = {marxes_2[marxes_2_start_offset:marxes_2_end_offset]}')

marxes_2.reverse()
print(f'marxes_2.reverse() -> {marxes_2}')
