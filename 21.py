for number in [29, 49]:
    divisors = 0
    for i in range(1, number + 1):
        if number % i == 0:
          divisors += 1
result = "Prime" if divisors == 2 else "Composite"
print(f"{number}: {result}")