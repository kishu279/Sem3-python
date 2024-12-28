# count the number of uppercase and lowercase letter from a sentence

str = input("Enter the string : ")

upperCount = 0
lowerCount = 0

for char in str :
    if char.isupper() :
        upperCount += 1
    elif char.islower():
        lowerCount += 1

print(f"{upperCount} UpperCase and {lowerCount} LowerCase letter")