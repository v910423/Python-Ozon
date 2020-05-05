import random


def do_bet(clientHourse, clientAmount):
    #global Bets
    if clientHourse > 10 or clientHourse < 1 or clientAmount <= 0:
        print('Please keep in mind that we have only 10 horses and you should give us money for betting on it.')
        return

    elif clientHourse in Bets.keys():
        print('Bet on this horse already exists. Choose another horse. ')
        return

    Bets[clientHourse] = clientAmount


Bets = {}
result = 'Y'
startRacing = str(input('Do u wanna make a bet? Y/N: ').capitalize())
if startRacing == "Y":

    while result == 'Y':
        amount = int(input('How much do you wanna bet?: '))
        horse = int(input('We have 10 horses. Which horse do you choose?: '))
        do_bet(horse, amount)
        result = str(input(str(Bets) + '\nFor making more bets, press Y: ').capitalize())

    print(str(Bets) + ' All bets are in. \nThe race starts now. \nThe winner is the horse number...' + str(
        random.randint(1, 10)) + "! Congratulations!")

else:
    print('See you soon.')
    exit()
