from utils import run_simulation
from parameters import (NUMBER_OF_FISHES, 
                        NUMBER_OF_SIMULATIONS, 
                        STEP_RANGE_START, 
                        STEP_RANGE_END, 
                        WIN_STEPS)

def main():
    list_of_boat_steps_to_check = list(range(STEP_RANGE_START, STEP_RANGE_END + 1, 1))
    for step in list_of_boat_steps_to_check:
        boat_win_count = 0
        fishes_win_count = 0
        for _ in range(NUMBER_OF_SIMULATIONS):
            winner, _ = run_simulation(step, NUMBER_OF_FISHES, WIN_STEPS)
            if winner == 'boat':
                boat_win_count += 1
            elif winner == 'fishes':
                fishes_win_count += 1
        total_wins = boat_win_count + fishes_win_count
        print(f"{step = }, boat_win_count = {boat_win_count/total_wins*100:.2f}%, fishes_win_count = {fishes_win_count/total_wins*100:.2f}%")
    return

if __name__ == '__main__':
    main()