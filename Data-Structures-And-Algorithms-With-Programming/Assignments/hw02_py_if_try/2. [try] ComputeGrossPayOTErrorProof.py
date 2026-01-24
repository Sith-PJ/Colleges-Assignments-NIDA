try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    if 0 <= hours <= 40:
        pay = hours * rate
        print("Pay:", int(pay))
    elif hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
        print("Pay:", int(pay))
    else:
        print("Error: Hours cannot be negative")
except:
    print("Error, please enter numeric input")