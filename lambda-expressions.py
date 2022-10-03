my_list = [1, 3, 4, 5, 6, 7, 8, 8, 9, 10, 12, 14]

# even numbers
new_list = list(filter(lambda x: (x % 2 == 0), my_list))

# just x2 elements of list
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_range = list(map(lambda x: x*2, current_list))
# print(new_range)


tables = [lambda x=x+1: x*10 for x in range(1, 11)]

for elem in tables:
    print(elem())


# max_number = lambda a, b: a if a > b else b
# print(max_number(5,3))
