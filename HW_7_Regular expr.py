import re

spisok = {}
answer = "Y"
quest = input('do u want to add user?: ').upper()
if quest != "Y":
    exit()
while answer == "Y":
    login = input("Введите логин. Он должен содержать более трех знаков и не должен содержать символы и пробелы. " )

    while not re.fullmatch(r'[A-z0-9]{3,}',login):
        login = input(('Введенный login не соответсвует формату. Повторите ввод: '))

    if re.fullmatch(r'[A-z0-9]{3,}',login):
        if login in spisok.values():
            print('Этот login уже занят.')
        else:
            email = input('Введите адрес электронной почты: ')  #v910423@gmail.com

            while not re.fullmatch(r'^[\w\-_\"\.]*@[a-z]+\.[a-z]+',email):
                email = input('Введенный адрес электронной почты не соответсвует формату. Повторите ввод почты: ')

            if re.fullmatch(r'\S*@\S*.\S',email):
                if email in spisok:
                    print('Этот адрес электронной почты уже занят для логина.')
                else:
                    spisok[email] = login
                    print('User is added.')

    answer = input('do u want to add user?: ').upper()
print(spisok)

with open("HW_7.txt", 'w') as file:
    file.write(str(spisok))
