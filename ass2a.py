# Without using a third variable (Tuple Unpacking)
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swap without a third variable
a, b = b, a

print(f"After swapping (without using third variable): a = {a}, b = {b}")
