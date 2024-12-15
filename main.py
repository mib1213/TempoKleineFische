from utils import run_simulation
from parameters import (NUMBER_OF_FISHES, 
                        NUMBER_OF_SIMULATIONS, 
                        STEP_RANGE_START, 
                        STEP_RANGE_END, 
                        WIN_STEPS,
                        RANDOM_STATE)

def main():
    list_of_boat_steps_to_check = list(range(STEP_RANGE_START, STEP_RANGE_END + 1))
    # since RANDOM_STATE is a global variable, it needs to be assigned to a local variable so that
    # it can be updated later
    random_state = RANDOM_STATE
    for step in list_of_boat_steps_to_check:
        boat_win_count = 0
        fishes_win_count = 0
        draw_count = 0
        for i in range(NUMBER_OF_SIMULATIONS):
            # we need to update the random_seed on every iteration, otherwise we would be giving the
            # same random_seed to the run_simulation function and will always be getting the same
            # winner, note that we are incrementing i everytime and not just 1 in order to get less
            # predictable results because think about another random_state that is being run in the
            # run_simulation function and also being incremented
            random_state += i
            winner, _ = run_simulation(step, NUMBER_OF_FISHES, WIN_STEPS, random_state)
            if winner == 'boat':
                boat_win_count += 1
            elif winner == 'fishes':
                fishes_win_count += 1

        total_wins = boat_win_count + fishes_win_count
        print(f"{step = }")
        print(f"boat_win_count = {boat_win_count/total_wins*100:.2f}%")
        print(f"fishes_win_count = {fishes_win_count/total_wins*100:.2f}%")
        print("-"*20)
    return

if __name__ == '__main__':
    main()