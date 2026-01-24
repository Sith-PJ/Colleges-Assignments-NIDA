numbers = []

while True:
    try:
        number = input("Enter a number: ")
        if number == 'done':
            break
        
        number = int(number)
        numbers.append(number)

    except ValueError:
        print("Invalid input")

print("Total:", sum(numbers))
print("Count:", len(numbers))
print("Average:", sum(numbers) / len(numbers) if len(numbers) > 0 else 0)