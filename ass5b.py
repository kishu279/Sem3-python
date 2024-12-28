# given student email and extract student roll number and institurte from the email

import re

email = input("Enter the student email : ")

# rollno = re.findall(r'\d+', email)

match = re.match(r'([a-zA-Z0-9]+)@([a-zA-z0-9.]+)', email)


if match :
    roll = match.group(1)
    institute = match.group(2)

    print(f"Roll number: {roll}")
    print(f"Institute Name: {institute}")
else :
    print("Invalid email format")