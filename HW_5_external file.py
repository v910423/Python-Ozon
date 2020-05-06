source = "/Users/valeriabelko/Desktop/Python/HW 5.txt"
with open(source) as file:
    text = file.read().split('\n')
    print(text)

    int_spisok = []
    for st in text:
        try:
            int_spisok.append(int(st))
        except ValueError:
            continue

    print(int_spisok)
    a = sum(int_spisok) / len(int_spisok)
    print(round(a,2))

#     spisok = [int(item) for item in text]

    summa = "Сумма чисел равна " + str(sum(int_spisok))
    avrg = "Среднее значение равно " + str(round(sum(int_spisok)/len(int_spisok),2))
    min = "Мин значение равно " + str(min(int_spisok))
    maks = "Max значение равно " + str(max(int_spisok))

results = '/Users/valeriabelko/Desktop/Python/Results.txt'
with open(results, 'w') as file2:
    file2.write(avrg + '\n' + summa + '\n' + min + '\n' + maks)



