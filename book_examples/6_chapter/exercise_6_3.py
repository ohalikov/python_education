guess_me = 5
for el in range(10):
    number = input("enter value: ")
    if int(number) < guess_me:
        print("too low")
        continue
    elif int(number) == guess_me:
        print("found it")
        break
    elif int(number) > guess_me:
        print("oops")
        continue
