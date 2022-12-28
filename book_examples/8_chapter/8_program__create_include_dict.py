# Включение словарей
# {выражение для ключа : выражение для значения нашего ключа for выражение in итерабельный объект}
word = 'my subject object gobject'
print(word.count('t'))
print(set(word))
letter_counts = {'буква - ' +
                 letter: f'встречается {word.count(letter)} раза' for letter in word}
print(letter_counts)
# метод word.count() будет несколько раз вызываться. Как этого избежать ?

# example 2
vowels = 'aeiou'
word = 'onomatopoeia'

vowel_counts = {letter: word.count(letter)
                for letter in set(word) if letter in vowels}
print(vowel_counts)
# тут мы превращаем слово в множество исключаем повторы и проверяем уникальную букву. входит ли она в vowels
