# def fact_rec(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact_rec(n-1)
# print(fact_rec(4))



def fact_line(n):
    return fact_iter(1,1,n)

def fact_iter(prod, counter, n):
    if counter > n:
        return prod
    else:
        return fact_iter(counter*prod, counter+1, n)

print(fact_line(4))