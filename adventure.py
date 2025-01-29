"""
Complete this file.
"""
PLAYER_HEALTH = 100
MONSTER_HEALTH = 70
HAS_TREASURE = False

import random
PATH = (random.choice(["left", "right"]))
print(f"go {PATH}")
if PATH == "left":
    print("You encounter a friendly gnome who heals you for 10 health points")
    HEALTH = int(PLAYER_HEALTH) + 10
    if HEALTH > 100:
        print("health is 100.")
if PATH == "right":
    print("You fall into a pit and lose 15 health points.")
    HEALTH = int(PLAYER_HEALTH) - 15
    print(f"Health is {HEALTH}.")
    if HEALTH < 0:
        print(f"health is {HEALTH}. You are barely alive!")

print("Combat Encounter")
MESSAGE = "Player goes first."
THREAT = "Monster's turn."
print(f"{MESSAGE} You strike the monster for 15 damage!")
DAMAGE = int(MONSTER_HEALTH) - 15
print(DAMAGE)
if DAMAGE <= 0:
    print("You defeated the monster!")
elif DAMAGE > 0:
    print(THREAT)
    import random
    ATTACK = random.random()
    if ATTACK < 0.5:
        print("The monster lands a critical hit for 20 damage!")
    else:
        print("The monster hits you for 10 damage!")
