func = lambda x, y: x + y
print(func(1,2))

def adder(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(('Sum:', sum))
adder(2,3,4,5,6,7,8)

#map
main_data = ['egor', 'petia', 'asia', 'kesha']
name_length = map(len, main_data)
print(list(name_length))

a, b = list(map(int, input().split()))

#filter
a = [1, -4, 6, 7, -10]
def func(x):
    if x > 0:
        return 1
    else:
        return 0
b = filter(func, a)
b = list(b)
print(b)

