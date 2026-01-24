def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Please enter a year in A.D.: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")
    

