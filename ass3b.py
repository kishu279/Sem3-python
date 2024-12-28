# python program to check whether if it is a leap year

year = int(input("Enter the year : "));
if (year % 4 == 0  or year % 400 == 0  ) :
  print(f"{year} is a leap year")
elif ( year % 100 == 0 ) :  # by 100 but not by 400 
  print ( " Not a leap year")
else :
  print(f"{year} is not a leap year.")

# correct order 400 -> 4 --> 100 for checking 