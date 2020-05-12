import random

def do_bet():
    global Bets
    clientHourse = int(input('We have 10 horses. Which horse do you choose?: '))
    while clientHourse > 10 or clientHourse < 1:
        print('Sorry, we have only 10 horses.')
        clientHourse = int(input('Which horse do you choose?: '))
    clientAmount = int(input('How much do you wanna bet?: '))
    while clientAmount <= 0:
        print('R u kidding me? Make your bet or go away!')
        clientAmount = int(input('How much do you wanna bet?: '))
    Bets[clientHourse] = clientAmount
    result = str(input(str(Bets) + '\nFor making more bets, press Y: ').capitalize())

    while str(result) == "Y":

        clientHourse = int(input('We have 10 horses. Which horse do you choose?: '))
        if clientHourse in Bets.keys():
            print('Bet on this horse already exists. Choose another horse. ')
        elif clientHourse > 10 or clientHourse < 1:
            print('Sorry, we have only 10 horses.')
        else:
            clientAmount = int(input('How much do you wanna bet?: '))
            while clientAmount <= 0:
                print('R u kidding me? Make your bet or go away!')
                clientAmount = int(input('How much do you wanna bet?: '))

            Bets[clientHourse] = clientAmount
            result = str(input(str(Bets) + '\nFor making more bets, press Y: ').capitalize())


Bets = {}
startRacing = str(input('Do u wanna make a bet? Y/N: ').capitalize())
if startRacing == "Y":
    do_bet()

    print(str(Bets) + ' All bets are in. \nThe race starts now. \nThe winner is the horse number...' + str(
        random.randint(1, 10)) + "! Congratulations!")

else:
    print('See you soon.')
    exit()
