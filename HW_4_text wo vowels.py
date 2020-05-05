#Простой вариант с переменной translatedText вне функции:

# def translate(text):
#     vowels = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", 'e', 'y', 'u', 'i', 'o', 'a']
#     newText = []
#     for i in range(len(text)):
#         if text[i] not in vowels:
#             newText.append(text[i])
#     return("".join(newText))
#
# text = input('Enter the text: ')
# translatedText = translate(text)
# print(translatedText)


#Вариант с глобальной переменной translatedText
def translate(text):
    vowels = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", 'e', 'y', 'u', 'i', 'o', 'a']
    global translatedText
    for letter in text:
        if letter not in vowels:
            translatedText.append(letter)

translatedText = []
text = input('Enter the text: ')
translate(text)
print("".join(translatedText))

