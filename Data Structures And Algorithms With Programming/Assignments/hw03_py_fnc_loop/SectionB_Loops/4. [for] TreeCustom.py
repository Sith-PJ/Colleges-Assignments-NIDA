tiers = int(input("Number of tiers: "))
for i in range (1, tiers + 1):
    print(" " * (tiers - i) + f"{i}" * ((i * 2) - 1))
print(" " * (tiers - 2) + "|.|")