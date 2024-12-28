# Write a python program which will take a single
# character from the user and check if the character is a vowel or consonant. If
# the input is neither a vowel nor consonant, then the code will show it is
# invalid input.

char = input(" Enter a single character : ")

if len(char)== 1 and char.isalpha() :
  char = char.lower()

  if char in "aeiou" :
    print(f"'{char}' is a vowel.");
  else :
    print(f"'{char}' is a consonant.")

else :
  print(" Invalid Input")