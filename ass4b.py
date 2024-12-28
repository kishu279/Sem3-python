# Python program to generate all prime numbers in given range


# Input the ending number from the user
end = int(input("Enter the ending number: "))

# Iterate through the range from 0 to the specified end
for num in range(2, end + 1):  # Start from 2, since 0 and 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")  # Print prime numbers
