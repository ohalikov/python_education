import copy

# deep copy
studentA_grades = [90, 85, 82]
studentB_grades = copy.deepcopy(studentA_grades)

studentB_grades.append(93)
print(studentA_grades)
print(studentB_grades)

# example 2
car_object = {
    "color": "grey",
    "functions": {
        "signal": "bib-bob",
        "handed": ["right", "left"]
    }
}

car2 = copy.deepcopy(car_object)

car2["speed"] = 300
print(car_object)
print(car2)

# Shallow copy
grades_1 = [966, 853, 822]
grades_2 = copy.copy(grades_1)
grades_2.append(888)
grades_1[0] = 555
print("grades 1 = {}".format(grades_1), "\ngrades 2 = {}".format(grades_2))


list1 = [1, 7, [3,5], 8]
list2 = copy.copy(list1)
print("\n\nThe original elements before shallow copying")
for i in range(0, len(list1)):
    print(list1[i], end=' ')

list2[2][0] = 10

print("\n\nThe original elements after shallow copying")
for i in range(0, len(list1)):
    print(list1[i], end=' ')

# ===================================================
# So we can not change inner elements in shallow copy
# ===================================================