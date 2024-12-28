# Write a program to convert upprercase letters into lowercase and lowercase letter into uppercase letters. ALso print the resultant string

str = input("Enter the string : ")
resultantStr = ""


for char in str :
    if char.islower() :
        resultantStr += char.upper()
    else :
        resultantStr += char.lower()

print(resultantStr)
