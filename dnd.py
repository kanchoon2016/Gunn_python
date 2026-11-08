boss_hp = 50


while boss_hp > 0:
  print("Dragon HP: " , boss_hp )
  damage = int(input("Enter your damage: "))
  boss_hp = boss_hp - damage
  print("the dragon has:", boss_hp)

print("Victory!,The dragon has been defeated")