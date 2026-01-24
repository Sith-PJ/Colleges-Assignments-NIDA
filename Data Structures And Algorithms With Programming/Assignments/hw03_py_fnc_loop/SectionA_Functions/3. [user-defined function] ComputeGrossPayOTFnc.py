def computepay(hours, rate):
    if hours < 0 or rate < 0:
        return "Error: Invalid Hours or Rate."
    
    if hours > 40:
        over_time = hours - 40
        regular_pay = 40 * rate
        overtime_pay = over_time * (rate * 1.5)
        return int(regular_pay + overtime_pay)
    else:
        return int(hours * rate)

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

print("Pay =", computepay(hours, rate))
