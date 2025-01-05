file = open("file.txt", "a")

n = int(input("Enter the number : "))

for i in range(2, n + 1) :
    for j in range(2, i) :
        if i % j == 0:
            break
    else :
        file.write(str(i))


