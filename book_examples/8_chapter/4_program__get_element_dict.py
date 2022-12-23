some_pythons = {
    'John': 'Cleese',
    'Graham': 'Chapman',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}

some_pythons['John']  # будет исключение

if 'Giyfre' in some_pythons:
    print("here")
elif 'Eric' in some_pythons:
    print("we are here")
else:
    print("not")


print(some_pythons.get('Michael2'))
