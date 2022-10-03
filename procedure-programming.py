patients = [
    {'name': 'Николай', 'height': 178},
    {'name': 'Иван', 'height': 182},
    {'name': 'Некоглай', 'height': 195}
]


total, count = 0, 0

for patient in patients: 
    total += patient['height']
    count += 1


print(total/3)


message = "Привет"
phrase = message


print(id(message))
print(id(phrase))