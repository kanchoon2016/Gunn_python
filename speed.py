limit = int(input("What is the limit on the sign: "))
speed = int(input("How fast are you going: "))

if speed <= limit:
    print("YOU are driving safely no fine")

elif speed <= limit+20:
    print("Waring you are speeding, your fine is 50$")

elif speed >= limit:
    print("You are driving too fast your fine is 150$")

else:
    print("error")