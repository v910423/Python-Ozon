# with open("/Users/valeriabelko/Downloads/Telegram Desktop/pi_million_digits.txt") as file:


path = 'pi_million_digits.txt'

with open(path) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line

birthday = input('enter ur bday: ')
# if birthday in pi_string:
#     print('success')
# else:
#     print('pity')

index = pi_string.find(birthday)
if index != -1:
    print(index)
    print(pi_string.count(birthday))
else:
    print('pity')

