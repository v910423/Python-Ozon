import random
print('Hello! Enter english words and its translation. I will make test.')

dictionary = {}

while True:
    key = input('Enter english word or Q: ').capitalize()
    if key == "Q":
        break
    value = input('Enter russian translation or Q: ').capitalize()
    if value == "Q":
        break
    dictionary[key] = value

flag = True
while flag:

    dictionary = list(dictionary.items())
    random.shuffle(dictionary)
    dictionary = dict(dictionary)

    print(dictionary)

    scores = 0
    errors = 0



    for key, value in dictionary.items():
        translation = input('Enter translation ' + key + ": ").lower()
        if translation == value:
            scores += 1
        else:
            errors += 1
        if errors == 3:
            print('Lose')
            break

    flag = input('Enter true if u want to play again: ')

    print(scores)