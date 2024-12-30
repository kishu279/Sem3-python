# take input as number and return nth fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Take input from the user
num = int(input("Enter a number: "))

# Print the nth Fibonacci number
print(f"Fibonacci: {fibonacci(num)}")
