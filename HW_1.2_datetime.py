
# Способ 1
#CurrDate = int(input("Please enter the year: "))
#if CurrDate%4 == 0:
#    print("It's the leap year")
#else: print ('Standard year')

# Способ 2
import datetime as dt
CurrDate = int(input("Please enter the year: "))
if (dt.datetime(CurrDate, 12, 31) - dt.datetime(CurrDate, 1, 1)).days == 365:
    print("It's the leap year")
else: print('Standard year')