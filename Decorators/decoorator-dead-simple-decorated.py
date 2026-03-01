import functools
import random

character = "Sir Bob"
health = 15
xp = 0


def characeter_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if health <= 0:
            print(f"{character} is too weak")
            return
        result = func(*args, **kwargs)
        print(f"{character} health {health} | XP: {xp}")
        return result
    return wrapper
    
    
@characeter_action
def eat_food(food):
    global health
    
    print(f"{character} ate {food}.")
    health += 1



@characeter_action
def fight_monster(monster, strength):
    global health, xp   

    if random.randint(1, 20) > strength:
        print(f"{character} fought {monster} and won!")
        xp += 10
    else:
        print(f"{character} flees from {monster} and lost!")
        health -= 10
        xp += 5
        

eat_food("bread")
fight_monster("Imp", 15)
fight_monster("Direwolf", 15)
fight_monster("Minotaur", 19)





