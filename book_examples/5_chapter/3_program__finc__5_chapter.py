poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))


word = 'the'

# find
print(poem.find(word))

# index
print(poem.index(word))

# rfind -> поиск с конца.
print(poem.rfind(word))
# rindex -> поиск с конца.
print(poem.rfind(word))

print(poem.count(word))  # сколько раз встречается the
print(poem.isalnum())


setup = 'a duck GoEsS into a bar...'
print(setup.strip('.'))

print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())  # Сменить регистры на противоположной


# ВЫравниевание
print(setup.center(50))
print(setup.ljust(50))
print(setup.rjust(50))
