day = int(input('day of birthday: '))

try:
    if day > 31 or day < 1:
        raise ValueError('неправильная дата')
except ValueError as msg:
    print('Ошибка', msg)