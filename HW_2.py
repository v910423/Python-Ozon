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

h = []

while attempts:
#for i in range(0,attempts):
    if len(h) != 0:
        print('You have ' + str(attempts) + " attempts left. You entered " + str(h))
    playernumber = float(input(('Enter the number: ' if len(h) != 0 else "Enter the number again: ")))

    if int(playernumber) == number:
        print("Win!!!")
        exit()
    elif playernumber in h:
        print ('You already entered this number.')
        #h.remove(playernumber)
        #attempts = attempts + 1
        continue
    elif (int(playernumber) > number) & (attempts != 1):
        print('Decrease your number')
    elif (int(playernumber) < number) & (attempts != 1):
        print('Increase your number')
    h.append(int(playernumber))

    attempts -= 1

print('You entered ' + str(h))


print("You lose. Correct number was " + str(number))