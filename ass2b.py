# AGP Calculation:
# AGP = 50% × basic pay

# Merged Basic Calculation:
# Merged Basic = Basic Pay + AGP

# DA Calculation:
# DA = 50% × Merged Basic

# HRA Calculation:
# HRA = 15% × Merged Basic

# Total Salary:
# Total Salary = Merged Basic + DA + HRA

basic_pay = float(input("Enter your base pay : "));
agp =  0.5 * basic_pay ;
merged_basic = basic_pay + agp ;
DA = 0.5 * merged_basic ;
hra = 0.15 * merged_basic ;
TotalSalary = merged_basic + DA + hra ;

print(f"Total salary of the employ is : {TotalSalary}")
