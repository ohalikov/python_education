from random import randrange

sum = (1 +
       2 +
       3 +
       4)
# print(sum)


x = 4
y = 5
z = 6

# if x < y < z:
#     print(f"{x}<{y}<{z}")

# print(bool(' '))


# Example 2
vowels = 'aeiou'
letter = 'o'
# if letter in vowels:
#     print(letter, 'is a vowel')


# Example 3
letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
vowel_dict = {'a': 'apple', 'e': 'elephant',
              'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
vowel_string = 'aeiou'
print(letter in vowel_list)


tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))


tweet_limit = 150
tweet_string = "Brah" * 50
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet 2")
else:
    print("Went over by 3", abs(diff))


secret_user_number = randrange(1, 10)
print(secret_user_number)

if guess := int(input("Gues number in range (1, 10): ")) == secret_user_number:
    print("congradulations, y")

else:
    print("YOU \"ARE\" LOSER")
