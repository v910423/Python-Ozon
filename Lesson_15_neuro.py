import random
import math

inches = 40
cm = 101.6

def neuro(epoch, rate, accur):
    W_coef = random.uniform(1,3)
    print(f"Первоначлаьный вес - {W_coef}")

    for i in range(epoch):
        err = cm - (inches*W_coef)

        if abs(err) < accur:
            print(F"Итог - {W_coef}")
        elif err > 0:
            W_coef += rate
        else:
            W_coef -= rate


epoch = int(input("Эпохи"))
lr = float(input("Скорость - "))
accur = float(input("Допустимая точность - "))

neuro(epoch, lr, accur)