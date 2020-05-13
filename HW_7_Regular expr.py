import re

while True:
    login = input("Введите логин. Он не должен содержать символы, должен начинаться с заглавной буквы, без проблеов" )
    print(re.fullmatch(r'[A-z0-9]{3,}',login))