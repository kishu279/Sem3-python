# sort the list of the string given according to the last element of each word


str = input("Enter the string : ")

str = str.split(" ")

def myFunc(word) :
    return word[-1]    

str.sort(key=myFunc)

print(str)