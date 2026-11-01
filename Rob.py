secret = "9999"
guess = ""

while guess != secret:
    guess = input("Enter the vault code!: ")
    if guess != secret:
        print("Wrong passcode")

print("The vault doors opens")
