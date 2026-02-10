# FIBONACCI
# 0 1 1 2 3 5 8 (0, 1, 0+1 -> 1, 1+1 -> 2, 1+2 -> 3, 2+3 -> 5, 3+5 -> 8)

def fibonacci_series(limit):
    a,b = 0,1
    for _ in range(limit):
        yield a
        a,b = b,a+b

f=fibonacci_series(7)
list1=list(f)
print(list1)

