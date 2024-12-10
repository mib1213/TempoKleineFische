import random
from utils import check_for_winner, boat_moves_forward, fish_moves_forward

def main():
    NUMBER_OF_FISHES = 4
    WIN_STEPS = 5
    initial_values = [0] * NUMBER_OF_FISHES

    fishes = {'steps': initial_values[:], 'caught_by_fisher?': initial_values[:], 'have_crossed_the_sea?': initial_values[:]}
    boat_steps = -5
    number_of_fishes_crossed_the_sea = 0
    number_of_fishes_caught_by_the_boat = 0
    counter = 0
    while True:
        print(f"{counter = }")
        winner = check_for_winner(number_of_fishes_caught_by_the_boat, 
                                number_of_fishes_crossed_the_sea, 
                                number_of_fishes=NUMBER_OF_FISHES)
        print(f"{winner = }")
        if winner == 'draw':
            break
        if winner == 'boat':
            print("Boat wins")
            break
        if winner == 'fishes':
            print("Fishes win")
            break
        dice = random.randint(0, NUMBER_OF_FISHES + 1)
        print(f"{dice = }")
        if dice == NUMBER_OF_FISHES or dice == NUMBER_OF_FISHES + 1:
            boat_steps, number_of_fishes_caught_by_the_boat, fishes['caught_by_fisher?'] = boat_moves_forward(boat_steps,
                                                                                                            fish_steps=fishes['steps'],
                                                                                                            caught_by_fisher=fishes['caught_by_fisher?'])     
            print(f"{boat_steps = }")
            print(f"{number_of_fishes_caught_by_the_boat = }")
            print(f"{fishes = }")                                    
        else:
            boat_steps, number_of_fishes_crossed_the_sea, fishes['steps'], fishes['have_crossed_the_sea?'] = fish_moves_forward(dice,
                                                                                                                                boat_steps,
                                                                                                                                number_of_fishes_crossed_the_sea,
                                                                                                                                fishes['steps'],
                                                                                                                                fishes['caught_by_fisher?'],
                                                                                                                                fishes['have_crossed_the_sea?'],
                                                                                                                                win_steps=WIN_STEPS)
            print(f"{boat_steps = }")
            print(f"{number_of_fishes_crossed_the_sea = }")
            print(f"{fishes = }")    
        counter += 1
        return

if __name__ == '__main__':
    main()