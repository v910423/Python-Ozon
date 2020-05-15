import re

spisok = {}
answer = "Y"
quest = input('do u want to add user?: ').upper()
if quest != "Y":
    exit()
while answer == "Y":
    login = input("Введите логин. Он должен содержать более трех знаков и начинаться с заглавной буквы, не должен содержать символы и пробелы. " )
    # result_login = re.fullmatch(r'[A-z0-9]{3,}',login)
    if re.fullmatch(r'[A-z0-9]{3,}',login):
        email = input('Введите адрес электронной почты: ')
        # result_email = re.fullmatch(r'\S*@\S*.\S',email)
        if re.fullmatch(r'\S*@\S*.\S',email):
            spisok[email] = login
        else:
            email = input('Введите адрес электронной почты: ')
    answer = input('do u want to add user?: ').upper()
# print(result_login)
# print(result_email)
print(spisok)
