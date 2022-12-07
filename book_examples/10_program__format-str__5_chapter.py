def sum(a, b):
    return a + b


actor = 'Richard Gere'
cat = 'Sam'
weight = 7

print("ma wife's favor actor is %s" % actor)
print("our cat %s witghts %s pounds" % (cat, weight))

print(f'{actor =} {weight =}')

print(f'{sum(5, 6) = }')

print(f'The {actor:>30} is the {cat:4^5}')
print(f'The {cat = :>10.3}')

song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""

print(song.replace(' m', ' M'))


questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

# first variant
for num_question, question in enumerate(questions):
    print(
        f'Q:{question}\nA:{answers[num_question]}\n')
# second variant
print("\n\n")
q_a = ((0, 1), (1, 2), (2, 0))
for q, a in q_a:
    print("Q:", questions[q])
    print("A:", answers[a])
    print()


print(f"My kitty cat likes %s," % 'roast beef')
print(f"My kitty cat likes %s," % 'ham')
print(f"My kitty cat fell on his %s" % 'head')
print(f"And now thinks he's a %s." % 'clam')
