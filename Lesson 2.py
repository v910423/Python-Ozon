# таблица умножения длинный способ
# for j in range(1,11):
#     number = []
#     for i in range(10):
#         number.append(j)
#     for i in range(1,11):
#         number[i-1] *= i
#     print(number)

# таблица умножения на 2
# numbers = [value * 2 for value in range(1,11)]
# print(*numbers)

# таблица умножения крутой способ
# numbers = [[value * i for value in range(1,11)] for i in range(1,11)]
# for elem in numbers:
#     print(*elem)

#Сортировка с реверсом
# number = int(input('Enter the number: '))
# stroka = str(number)
# spisok = list(stroka)
# #sorted_spisok = reversed(sorted(spisok))
# #sorted_spisok = sorted(spisok, reverse=True)
# #spisok = spisok[::-1]
# spisok.sort()
# spisok.reverse()
# res_stroka = ''.join(spisok)
# print(int(res_stroka))
# #print(spisok)
# #print(sorted_spisok)

import random

#num = int(input('quantity of bullets? '))
bullets = [0 for i in range(6)]
bullets[0] = 1
print(bullets)
a = int(input('Do u want to play? Y = 1, N = 0 '))
while a == 1:
    if random.choice(bullets) == 0:
        print('Lose. Again?')
    else:
        print('Win.Again?')
    a = int(input('Y = 1, N = 0 '))
print('Great game.')