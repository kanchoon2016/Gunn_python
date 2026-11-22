prize = 2500
net_prize = prize * (1 - 0.05)
hand_answer = float(input("Enter your hand answer: "))
if abs(hand_answer - net_prize) < 0.001:
    print("Correct!")
else:
     print("Try again.")
