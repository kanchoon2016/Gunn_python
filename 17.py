factors = []
for i in range(1, 25):
    if 24 % i == 0:
        factors.append(i)
print("Factors:", factors)
print("Count:", len(factors))