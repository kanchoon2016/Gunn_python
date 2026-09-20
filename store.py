items= int(input("the total price of the item is: "))
Price=int(input("how much money: "))


if Price == items:
    print("Exact amunt received,no change required")

if Price>=items:
    print("payment succesful,here is your change is: ")
    change= Price-items
    print("this is your change: ",change)
if Price<=items:
    print("Not enough money.You still need to pay: ")





