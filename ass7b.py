# print a series of fibonacci upto n terms

num = int(input("Enter a number: "))

def fibonacci_s(num) :
    a, b = 0, 1
    
    fib_series = []

    for _ in range(num) :
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

print(f"{fibonacci_s(num)}")