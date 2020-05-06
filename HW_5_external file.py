source = "/Users/valeriabelko/Desktop/Python/HW 5.txt"
with open(source) as file:
    text = file.read().split('\n')
    try:
        spisok = [int(item) for item in text]
    except:
        continue

    summa = "Сумма чисел равна " + str(sum(spisok))
    avrg = "Среднее значение равно " + str(sum(spisok)/len(spisok))

results = '/Users/valeriabelko/Desktop/Python/Results.txt'
with open(results, 'w') as file2:
    file2.write(avrg + '\n' + summa)

