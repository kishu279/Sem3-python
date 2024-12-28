# find second maximum and second minimum numbers in the list


num = [12, 35, 1, 10, 34, 1]

def maxMin(num) :
    num.sort()

    if len(num) < 3:
        print("There is no second maximum and second minimum")
        return 

    print(f"second minimum : {num[1]}")        

    print(f"second maximum : {num[len(num) - 2]}")

maxMin(num)

