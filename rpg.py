hp = int(input("input your hp:"))


if hp<=30:
    print("You are getting low on hp,DO YOU WANT TO ATTACK OR HEAL")
    action =input("choose your action: ")
    if action == "attack":
        print("It was too risky,you fainted")
    if action =="Heal":
        newhp = hp+50
        print("Your new hp: ",newhp)

elif hp>=30:
    print("you are healthy,do you want to Heal or attack")
    action =input("choose your action: ")

    if action =="attack": 
     print("YOU killed the monster, you earn 5 gold and 10 xp")
    if action =="Heal":
       print("your hp is high enough,You wasted a turn")
   
    