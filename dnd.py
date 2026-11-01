boss_hp = 50
damage = ""


while boss_hp >= 10:
  boss_hp = boss_hp - damage
  damgae = input("Enter your damage again: ")
  if boss_hp - damage:
    print("the dragon has:", boss_hp)

print("Victory!,The dragon has been defeated")