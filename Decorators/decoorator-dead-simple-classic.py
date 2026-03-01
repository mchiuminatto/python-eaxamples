import random

character = "Sir Bob"
health = 15
xp = 0


# Raw functions without decorators

def eat_food(food):
    global health
    if health < 0:
        print(f"{character} is too weak")
        return
    
    print(f"{character} ate {food}.")
    health += 1
    print(f"{character} health {health} | XP: {xp}")


def fight_monster(monster, strength):
    global health, xp   
    if health < 0:
        print(f"{character} is too weak")
        return

    if random.randint(1, 20) > strength:
        print(f"{character} fought {monster} and won!")
        xp += 10
    else:
        print(f"{character} flees from {monster} and lost!")
        health -= 10
        xp += 5
        
    print(f"{character} health {health} | XP: {xp}")


eat_food("bread")
fight_monster("Imp", 15)
fight_monster("Direwolf", 15)
fight_monster("Minotaur", 19)





