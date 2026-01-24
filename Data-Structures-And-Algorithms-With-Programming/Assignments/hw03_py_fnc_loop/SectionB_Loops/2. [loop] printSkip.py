begin = int(input("Begin: "))
end = int(input("End: "))
step = int(input("Step: "))
i = begin
numbers = []

while i < end:
    numbers.append(str(i))
    i += step

print(" ".join(numbers))