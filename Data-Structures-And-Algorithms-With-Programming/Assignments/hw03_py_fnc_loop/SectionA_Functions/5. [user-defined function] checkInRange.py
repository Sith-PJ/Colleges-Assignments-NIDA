def isInRange(lower_bound, upper_bound, number):
    return lower_bound <= number <= upper_bound

lower_bound = float(input("Lower bound: "))
upper_bound = float(input("Upper bound: "))
number = float(input("Number: "))

try:
    if isInRange(lower_bound, upper_bound, number):
        print(f"{number:g} is within the range [{lower_bound:g},{upper_bound:g}]")
    else:
        print(f"{number:g} is out of the range [{lower_bound:g},{upper_bound:g}]")
except ValueError:
    print("Error: Invalid input.")