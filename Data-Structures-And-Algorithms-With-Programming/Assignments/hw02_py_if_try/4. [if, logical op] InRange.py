def isInRange(number):
    return 900 <= number <= 1100 or 1900 <= number <= 2100

number = int(input("Enter a number: "))
print(isInRange(number))