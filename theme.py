
height = int(input("how tall are you: "))

if height<120:
    print("Sorry, you are not tall enough to ride")

elif height>=120:
    print("You can ride,But whats your age")
    Age = int(input("What is your age: "))
    if Age<12:
        print("That will be $5")

    elif Age>=12 and Age<=18:
        print("that would be $7")

    else:
        print("That is $12")
