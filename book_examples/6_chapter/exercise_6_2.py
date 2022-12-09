#
guess_me = 7
# start_number = 1

while True:
    start_number = input("enter start value [write q for exit]: ")
    if start_number == 'q':
        break
    elif int(start_number) < guess_me:
        print("too low")
        continue
    elif int(start_number) == guess_me:
        print("found it")
        break
    elif int(start_number) > guess_me:
        print("oops")
        continue
