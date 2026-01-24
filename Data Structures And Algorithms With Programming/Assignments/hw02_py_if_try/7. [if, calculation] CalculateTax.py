income = int(input("Income: "))

if income <= 10000:
    print("Tax: None")
elif 10000 <= income <= 20000:
    tax = (income - 10000) * 0.1
    print("Tax:", tax)
elif income > 20000:
    tax = (income - 20000) * 0.2 + 1000
    print("Tax:", tax)
else:
    print("Invalid income")