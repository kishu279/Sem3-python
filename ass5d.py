# accepts the sentence from user and also take two positions to extract the substring and check that substring is pallindrome or not

def check(str, pos1, pos2) :
    if pos1 < 0 or pos2 >= len(str) or pos1 > pos2 :
        print("Invalid Positions")
        return 

    tmp = str[pos1: pos2 + 1]

    rev = tmp[::-1]

    if rev == tmp :
        print(f"{tmp} is a Pallindrome")
    else :
        print(f"{tmp} not a Pallindrome")

str = input("Enter the sentence : ")
pos1 = int(input("Enter the position 1 : "))
pos2 = int(input("Enter the position 2 : "))

check(str, pos1, pos2)
