common = []
for i in range(1, 51):
    if i % 4 == 0 and i % 6 == 0:
        common.append(i)
print("Common multiples:", common)
print("Count:", len(common))