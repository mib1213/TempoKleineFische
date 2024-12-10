import random
from utils import check_for_winner, boat_moves_forward, fish_moves_forward

def main():
    NUMBER_OF_FISHES = 4
    NUMBER_OF_SIMULATIONS = 10000
    STEP_RANGE_START = -10
    STEP_RANGE_END = -1
    WIN_STEPS = 5

    initial_values = [0] * NUMBER_OF_FISHES
    list_of_boat_steps_to_check = list(range(STEP_RANGE_START, STEP_RANGE_END + 1, 1))

    for step in list_of_boat_steps_to_check:
        boat_win_count = 0
        fishes_win_count = 0
        for _ in range(NUMBER_OF_SIMULATIONS):
            fishes = {'steps': initial_values[:], 'caught_by_fisher?': initial_values[:], 'have_crossed_the_sea?': initial_values[:]}
            boat_steps = step
            number_of_fishes_crossed_the_sea = 0
            number_of_fishes_caught_by_the_boat = 0
            while True:
                winner = check_for_winner(number_of_fishes_caught_by_the_boat, 
                                        number_of_fishes_crossed_the_sea, 
                                        number_of_fishes=NUMBER_OF_FISHES)
                if winner == 'draw':
                    break
                if winner == 'boat':
                    boat_win_count += 1
                    break
                if winner == 'fishes':
                    fishes_win_count += 1
                    break
                dice = random.randint(0, NUMBER_OF_FISHES + 1)
                if dice == NUMBER_OF_FISHES or dice == NUMBER_OF_FISHES + 1:
                    boat_steps, number_of_fishes_caught_by_the_boat, fishes['caught_by_fisher?'] = boat_moves_forward(boat_steps,
                                                                                                                      fish_steps=fishes['steps'],
                                                                                                                      caught_by_fisher=fishes['caught_by_fisher?'])                                         
                else:
                    boat_steps, number_of_fishes_crossed_the_sea, fishes['steps'], fishes['have_crossed_the_sea?'] = fish_moves_forward(dice,
                                                                                                                                        boat_steps,
                                                                                                                                        number_of_fishes_crossed_the_sea,
                                                                                                                                        fishes['steps'],
                                                                                                                                        fishes['caught_by_fisher?'],
                                                                                                                                        fishes['have_crossed_the_sea?'],
                                                                                                                                        win_steps=WIN_STEPS)
        total_wins = boat_win_count + fishes_win_count
        print(f"{step = }, boat_win_count = {boat_win_count/total_wins*100:.2f}%, fishes_win_count = {fishes_win_count/total_wins*100:.2f}%")
    return

if __name__ == '__main__':
    main()