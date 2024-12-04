import random

dice = [range(6)]

boat_steps = 0
fish_1_steps = 0
fish_2_steps = 0
fish_3_steps = 0
fish_4_steps = 0

fish_1, fish_2, fish_3, fish_4 = 1, 1, 1, 1 # they are in the game
fish_1_status, fish_2_status, fish_3_status, fish_4_status = 0, 0, 0, 0

for i in range(100):
    dice = random.randint(0, 5)
    if dice == 0 or dice == 5:
        boat_steps += 1
        if boat_steps >= fish_1_steps:
            fish_1 = 0
        elif boat_steps >= fish_2_steps:
            fish_2 = 0
        elif boat_steps >= fish_3_steps:
            fish_3 = 0
        elif boat_steps >= fish_4_steps:
            fish_4 = 0
    elif dice == 1:
        if fish_1:
            if fish_1_steps < 10:
                fish_1_steps += 1
            else:
                fish_1_status = 1
        else:
            boat_steps += 1
    elif dice == 2:
        if fish_2:
            if fish_2_steps < 10:
                fish_2_steps += 1
            else:
                fish_2_status = 1
        else:
            boat_steps += 1
    elif dice == 3:
        if fish_3:
            if fish_3_steps < 10:
                fish_3_steps += 1
            else:
                fish_3_status = 1
        else:
            boat_steps += 1
    else:
        if fish_4:
            if fish_4_steps < 10:
                fish_4_steps += 1
            else:
                fish_4_status = 1
        else:
            boat_steps += 1

print(f"{boat_steps = }, {fish_1_steps = }, {fish_2_steps = }, {fish_3_steps = }, {fish_4_steps = }")
print(f"{fish_1_status = }, {fish_2_status = }, {fish_3_status = }, {fish_4_status = }")