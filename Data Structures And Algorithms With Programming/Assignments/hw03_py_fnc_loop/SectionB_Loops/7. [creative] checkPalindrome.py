number = input("Please enter a number: ")
if number != number[::-1]:
    print(f"{number} is NOT a palindrome.")
else:
    print(f"{number} is a palindrome.")