def palindrome(a):
    if a == a[::-1]:
        print('It is palindrom')
    else:
        print("It is not palindrom")

# вариант 2:
def palindrom_v2(a):
    length = len(a)
    for i in range(int(length // 2)):
        if a[i] != a[-1 - i]:
            print('It is not palindrom')
            exit()
    print('It is palindrom')

text = list(input('Enter the word: '))
palindrom_v2(text)
