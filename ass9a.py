# A string with parenthesis check for the opening and closing 

def wellBracketed(str) :
    bracketList = {
        "()": 0,
        "{}": 0,
        "[]": 0,
    }

    for chr in str :
        for key in bracketList.keys() :
            if chr in key[0] :
                bracketList[key] += 1
            elif chr in key[1] :
                bracketList[key] -= 1

            if bracketList[key] == -1 :
                return False
    

    for value in bracketList.values() :
        if value != 0 :
            return False
    
    return True

# str = input("Enter the String: ")


def rotationList(str, rot) :
    if rot > 0 :
        remList = str[-rot:]
        str = str[:-rot]

        remList[::-1]
        return remList + str
    elif rot < 0 :
        rot = -rot

        remList = str[:rot]
        str = str[rot:]

        return str + remList

str = "sourav"

print(f"Well bracketed: {wellBracketed(str)}")

rotatedList = rotationList(str, -2)
print(rotatedList)