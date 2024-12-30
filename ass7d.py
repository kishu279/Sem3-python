# use lambda function to print all leap years from 2024 to 3010

yearList = range(2024, 3011)

leapYears = list(filter(lambda year: (year%4 == 0 and year%100 != 0) or (year%400 == 0), yearList))

print(f"The list of all leap years from 2024 to 3010 {leapYears}")