string = r'''
    Boys and girls, come out to play.
    The moon doth shine as bright like a dimond
'''

string2 = r'Type a \n to get a new line is a normal string'

start = '\n' + 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(string)
print(string2)
print(start + start + middle + end)
