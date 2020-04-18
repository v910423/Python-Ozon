import random
#print(random.randint(1, 20))

number = random.randint(1, 10)
print('You have 5 attempts')
playernumber = int(input('Enter the number: '))

i = 1
for i in 5:

    if playernumber == number:
        print("Win!!!")
    else:
        print("Lose")
        playernumber = int(input('Enter the number again: '))

print("Correct number was " + str(number))