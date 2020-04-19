import random
number = random.randint(1, 50)
Level = input('Choose your level: beginner/intermediate/advanced: ').strip().capitalize()

while Level != "Beginner" and Level != "Advanced" and Level != "Intermediate":
    print('You should make ur choice. Enter valid option. If you don"t want to play, press Q')
    Level = input('Choose your level: beginner/intermediate/advanced: ').strip().capitalize()
    if Level == "Q":
            print("Bye!")
            quit()

if Level == "Beginner":
    attempts = 12
elif Level == "Intermediate":
    attempts = 9
elif Level == "Advanced":
    attempts = 6

print('You have ' + str(attempts) + ' attempts')

for i in range(0,attempts):
    playernumber = int(input('Enter the number: ' if i==0 else "Enter the number again: "))

    if playernumber == number:
        print("Win!!!")
        exit()
    elif (playernumber > number) & (i != attempts - 1):
        print('Decrease your number')
    elif (playernumber < number) & (i != attempts - 1):
        print('Increase your number')

print("You lose. Correct number was " + str(number))