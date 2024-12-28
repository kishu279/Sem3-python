# accept sentence from user as input and below 
# a. unique common words
# b. all unique words
# c. all unique words present in 1st statement but not in second

str1 = input("Enter sentence 1: ")
str2 = input("Enter sentence 2: ")

str1 = set(str1.split(" "))
str2 = set(str2.split(" "))

common_words = str1.intersection(str2)
print(common_words)

all_unique_words = str1.union(str2)
print(all_unique_words)

unique_in_first = str1.difference(str2)
print(unique_in_first)

