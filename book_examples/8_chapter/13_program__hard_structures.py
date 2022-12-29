marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges

print(tuple_of_lists)
tuple_of_lists[1][1] = 'afsdfasd'
# tuple_of_lists[1] = ''
print(tuple_of_lists)


list_of_lists = [marxes, pythons, stooges]
# [['Groucho', 'Chico', 'Harpo'], ['Chapman', 'afsdfasd', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry']]
print(list_of_lists)

print()
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)


houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
}


print(houses[(38.89, -77.03, 13)])
