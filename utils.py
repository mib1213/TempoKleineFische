import random
from typing import Literal, TypeAlias

def check_for_winner(number_of_fishes_caught_by_the_boat: int, 
                     number_of_fishes_crossed_the_sea: int, 
                     number_of_fishes: int) -> Literal['draw', 'boat', 'fishes'] | None:
    half_of_number_of_fishes: int = number_of_fishes // 2 
    # float division in case number of fishes is an odd number
    if number_of_fishes_caught_by_the_boat == half_of_number_of_fishes \
        and number_of_fishes_crossed_the_sea == half_of_number_of_fishes:
        return 'draw'
    if number_of_fishes_caught_by_the_boat >= half_of_number_of_fishes + 1:
        return 'boat'
    if number_of_fishes_crossed_the_sea >= half_of_number_of_fishes + 1:
        return 'fishes'
    return None

boat_return: TypeAlias = tuple[int, int, list[bool]]

def boat_moves_forward(boat_steps: int, 
                       fish_steps_list: list[int], 
                       caught_by_fisher: list[bool]) -> boat_return:
    boat_steps += 1
    number_of_fishes_caught_by_the_boat: int = 0
    # number of fishes caught by the boat variable needs to be set to 0 everytime this function
    # is called, the reason being the for loop below calculates the TOTAL number of fishes caught
    # by the boat everytime, so even if there were fishes caught before, the below for loop will 
    # count them again.
    for i, fish_steps in enumerate(fish_steps_list):
        if boat_steps >= fish_steps:
            caught_by_fisher[i] = 1
            number_of_fishes_caught_by_the_boat += 1
    return (boat_steps, 
            number_of_fishes_caught_by_the_boat, 
            caught_by_fisher)

fish_return: TypeAlias = tuple[int, int, list[int], list[bool]]

def fish_moves_forward(dice: int,
                       boat_steps: int,
                       number_of_fishes_crossed_the_sea: int,
                       win_steps: int, 
                       fish_steps: list[int],
                       caught_by_fisher_list: list[bool],
                       have_crossed_the_sea_list: list[bool]) -> fish_return:
    enumerated: enumerate = enumerate(zip(caught_by_fisher_list, have_crossed_the_sea_list))
    for i, (caught_by_fisher, have_crossed_the_sea) in enumerated:
        if dice == i:
            if not caught_by_fisher:
                if not have_crossed_the_sea:
                    fish_steps[i] += 1
                    if fish_steps[i] == win_steps:
                        have_crossed_the_sea_list[i] = 1
                        number_of_fishes_crossed_the_sea += 1
                else:
                    for j, (caught_by_fisher_inner, have_crossed_the_sea_inner) in enumerated:
                        if not caught_by_fisher_inner and not have_crossed_the_sea_inner:
                            fish_steps[j] += 1
                            if fish_steps[j] == win_steps:
                                have_crossed_the_sea_list[j] = 1
                                number_of_fishes_crossed_the_sea += 1
                            break                                        
            else:
                boat_steps += 1

    return (boat_steps, 
            number_of_fishes_crossed_the_sea, 
            fish_steps, 
            have_crossed_the_sea_list)

simulation_return: TypeAlias = tuple[str, dict[str: list[int] | list[bool]]]
simulation: TypeAlias = dict[str: list[int | tuple[int] | tuple[bool]]]

def run_simulation(step: int, 
                   number_of_fishes: int, 
                   win_steps: int, 
                   random_state: int = None) -> simulation_return:
    initial_values: list[0] = [0] * number_of_fishes

    fish_steps: list[int] = initial_values[:]
    caught_by_fisher: list[bool] = initial_values[:]
    have_crossed_the_sea: list[bool] = initial_values[:]
    boat_steps: int = step
    number_of_fishes_crossed_the_sea: int = 0
    number_of_fishes_caught_by_the_boat: int = 0
    counter: int = 0

    simulation_output: simulation = {'counter': [],                                        
                                     'winner': [], 
                                     'dice': [],
                                     'boat_steps': [],
                                     'number_of_fishes_caught_by_the_boat': [],
                                     'number_of_fishes_crossed_the_sea': [],
                                     'fish_steps': [],
                                     'caught_by_fisher': [],
                                     'have_crossed_the_sea': []}
    while True:
        simulation_output['counter'].append(counter)
        winner: str | None = check_for_winner(number_of_fishes_caught_by_the_boat, 
                                              number_of_fishes_crossed_the_sea, 
                                              number_of_fishes=number_of_fishes)
        simulation_output['winner'].append(winner)

        if winner:
            break
        if random_state:
            random.seed(random_state)
            random_state += counter
        dice: int = random.randint(0, number_of_fishes + 1)
        
        if dice == number_of_fishes or dice == number_of_fishes + 1:
            boat_move_return: boat_return = boat_moves_forward(boat_steps, 
                                                               fish_steps,
                                                               caught_by_fisher)
            boat_steps: int = boat_move_return[0]
            number_of_fishes_caught_by_the_boat: int = boat_move_return[1]
            caught_by_fisher: list[bool] = boat_move_return[2]                          
        else:
            fishes_move_return: fish_return = fish_moves_forward(dice,
                                                                 boat_steps,
                                                                 number_of_fishes_crossed_the_sea,
                                                                 win_steps,
                                                                 fish_steps,
                                                                 caught_by_fisher,
                                                                 have_crossed_the_sea)
            boat_steps: int = fishes_move_return[0]
            number_of_fishes_crossed_the_sea: int = fishes_move_return[1]
            fish_steps: list[int] = fishes_move_return[2]
            have_crossed_the_sea: list[bool] = fishes_move_return[3]
        counter += 1
        simulation_output['dice'].append(dice)
        simulation_output['boat_steps'].append(boat_steps)
        simulation_output['number_of_fishes_caught_by_the_boat'].append(number_of_fishes_caught_by_the_boat)
        simulation_output['number_of_fishes_crossed_the_sea'].append(number_of_fishes_crossed_the_sea)
        simulation_output['fish_steps'].append(tuple(fish_steps))
        simulation_output['caught_by_fisher'].append(tuple(caught_by_fisher))
        simulation_output['have_crossed_the_sea'].append(tuple(have_crossed_the_sea))

    len_counter = len(simulation_output['counter'])
    for key in simulation_output.keys():     
        if len(simulation_output[key]) < len_counter:
            simulation_output[key].append(None)

    return winner, simulation_output