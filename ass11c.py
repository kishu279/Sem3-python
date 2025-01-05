file = open("file.txt", 'w')

n = int(input("enter the number : "))

file.write('0\n')
file.close()

file = open("file.txt", 'a')

a = 0
b = 1

for i in range(2, n + 1) :
    a, b = b, a + b
    file.write(str(a) + '\n')


file.close()