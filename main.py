print("välj din typ av karaktär!")
print("1.offensiv")
print("2.deffensiv")

import random

spelare_hp = 100
fiende_hp = 80

while spelare_hp > 0 and fiende_hp > 0:
    spelare_slag = random.randint(8, 18)
    fiende_slag = random.randint(1, 10) 
    spelare_hp -= fiende_slag
    print(f"Du: {max(0,spelare_hp)} HP | Fiende: {max(0,fiende_hp)} HP")

if spelare_hp > 0:
    print("Du vann!")
else:
    print("Fienden vann.")