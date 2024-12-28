# take a string as input and make a dictionary of keys of unique words and frequency as value

str = input("Enter the string: ")

str = str.split(" ")
wordFreq = dict()

for i in str :  
    wordFreq[i] = wordFreq.get(i, 0) + 1

print(wordFreq)