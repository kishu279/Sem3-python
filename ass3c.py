import math

# Accepting coefficients a, b, and c from the user
a = float(input("Enter the coefficient a (a ≠ 0): "))
if a == 0:
    print("Invalid input. 'a' must not be 0.")
else:
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the constant term c: "))

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Determine the nature of the roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The roots are real and equal: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex and distinct: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
