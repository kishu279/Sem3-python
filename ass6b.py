# take a list and make a new list according to the indexing in the first list and put 0 if element not present in list 1


num = [1, 2, 5]
newList = []

for i in range(0, max(num) + 1) :
    if i not in num :
        newList.append(0)
    else :
        newList.append(i)

print(newList)
    