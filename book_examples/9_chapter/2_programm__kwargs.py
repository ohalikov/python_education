# def print_kwargs(**kwargs):
#     print(list(kwargs))
#     print('keyword arguments:', kwargs)
    

# print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# =================================
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)
        

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)