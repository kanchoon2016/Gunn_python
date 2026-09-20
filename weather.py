celsius = int(input("forecast says the weather is °C: "))

if celsius<15:
    print("You should wear a heavy coat")

elif celsius>15 and celsius<25:
    print("The weather is pleasant, a light jacket is fine")

elif celsius>25:
    print("Its hot outside,wear a t-shirt")

else:
    print("error")