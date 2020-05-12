import re

# text = input()
# result = re.match(r'...',text)
# print(result.group(0))

# text = input()
# result = re.search(r'...',text)   #ищет по всей строке
# print(result.group(0))

# text = input()
# result = re.findall(r'[a-zА-яа-я][0-9]',text)
# print(result)

# text = input()
# result = re.findall(r'[\w\d\s\b]',text) #\w - любая цифра и буква  \d - любоя цифр, \s - space, \b - граница слова. Если набрать букву с большой буквы то это означает все символы кроме проблеа или кроме цифр или тд
# print(result)

text = input()
# result = re.findall(r'^[\w_\.\-]+@\w+\.\w+$',text)
# print(result)  #cdfvc v9104@gmail.com

#проверка на тел +7 123 1122233
result2 = re.match(r'(\+7|8)( |)\d{3}( |)\d{7}', text)
if result2:
    print(result2.group(0))
else:
    print('not phone number')