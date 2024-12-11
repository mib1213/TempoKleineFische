import random
import copy

def check_for_winner(number_of_fishes_caught_by_the_boat, 
                    number_of_fishes_crossed_the_sea, 
                    number_of_fishes):
    half_of_number_of_fishes = number_of_fishes // 2 
    if number_of_fishes_caught_by_the_boat == half_of_number_of_fishes \
        and number_of_fishes_crossed_the_sea == half_of_number_of_fishes:
        return 'draw'
    if number_of_fishes_caught_by_the_boat >= half_of_number_of_fishes + 1:
        return 'boat'
    if number_of_fishes_crossed_the_sea >= half_of_number_of_fishes + 1:
        return 'fishes'
    return None

def boat_moves_forward(boat_steps,
                fish_steps,
                caught_by_fisher):
    boat_steps += 1
    number_of_fishes_caught_by_the_boat = 0
    for i, fish_steps in enumerate(fish_steps):
        if boat_steps >= fish_steps:
            caught_by_fisher[i] = 1
            number_of_fishes_caught_by_the_boat += 1
    return boat_steps, number_of_fishes_caught_by_the_boat, caught_by_fisher

def fish_moves_forward(dice,
                       boat_steps,
                       number_of_fishes_crossed_the_sea,
                       win_steps, 
                       fish_steps_list,
                       caught_by_fisher_list,
                       have_crossed_the_sea_list):
    for i, (caught_by_fisher, have_crossed_the_sea) \
        in enumerate(zip(caught_by_fisher_list, have_crossed_the_sea_list)):
        if dice == i:
            if not caught_by_fisher:
                if not have_crossed_the_sea:
                    fish_steps_list[i] += 1
                    if fish_steps_list[i] == win_steps:
                        have_crossed_the_sea_list[i] = 1
                        number_of_fishes_crossed_the_sea += 1
                else:
                    for j, (caught_by_fisher_inner, have_crossed_the_sea_inner) \
                        in enumerate(zip(caught_by_fisher_list, have_crossed_the_sea_list)):
                        if not caught_by_fisher_inner:
                            if not have_crossed_the_sea_inner:
                                    fish_steps_list[j] += 1
                                    if fish_steps_list[j] == win_steps:
                                        have_crossed_the_sea_list[j] = 1
                                        number_of_fishes_crossed_the_sea += 1
                                    break                                        
            else:
                boat_steps += 1
    return boat_steps, number_of_fishes_crossed_the_sea, fish_steps_list, have_crossed_the_sea_list

def run_simulation(step, number_of_fishes, win_steps):
    initial_values = [0] * number_of_fishes

    fishes = {'steps': initial_values[:], 
              'caught_by_fisher?': initial_values[:], 
              'have_crossed_the_sea?': initial_values[:]}
    boat_steps = step
    number_of_fishes_crossed_the_sea = 0
    number_of_fishes_caught_by_the_boat = 0
    counter = 0

    simulation_output = {'counter': [], 
                         'winner': [], 
                         'dice': [],
                         'boat_steps': [],
                         'number_of_fishes_caught_by_the_boat': [],
                         'number_of_fishes_crossed_the_sea': [],
                         'fishes': []}
    while True:
        simulation_output['counter'].append(counter)
        winner = check_for_winner(number_of_fishes_caught_by_the_boat, 
                                  number_of_fishes_crossed_the_sea, 
                                  number_of_fishes=number_of_fishes)
        simulation_output['winner'].append(winner)

        if winner:
            break
        dice = random.randint(0, number_of_fishes + 1)
        
        if dice == number_of_fishes or dice == number_of_fishes + 1:
            boat_move_return = boat_moves_forward(boat_steps, 
                                                  fish_steps=fishes['steps'],
                                                  caught_by_fisher=fishes['caught_by_fisher?'])
            boat_steps = boat_move_return[0]
            number_of_fishes_caught_by_the_boat = boat_move_return[1]
            fishes['caught_by_fisher?'] = boat_move_return[2]                          
        else:
            fishes_move_return = fish_moves_forward(dice,
                                                    boat_steps,
                                                    number_of_fishes_crossed_the_sea,
                                                    win_steps,
                                                    fishes['steps'],
                                                    fishes['caught_by_fisher?'],
                                                    fishes['have_crossed_the_sea?'])
            boat_steps = fishes_move_return[0]
            number_of_fishes_crossed_the_sea = fishes_move_return[1]
            fishes['steps'] = fishes_move_return[2]
            fishes['have_crossed_the_sea?'] = fishes_move_return[3]
        counter += 1
        simulation_output['dice'].append(dice)
        simulation_output['boat_steps'].append(boat_steps)
        simulation_output['number_of_fishes_caught_by_the_boat'].append(number_of_fishes_caught_by_the_boat)
        simulation_output['number_of_fishes_crossed_the_sea'].append(number_of_fishes_crossed_the_sea)
        simulation_output['fishes'].append(copy.deepcopy(fishes))

    
    simulation_output['dice'].append(None)
    simulation_output['boat_steps'].append(None)
    simulation_output['number_of_fishes_caught_by_the_boat'].append(None)
    simulation_output['number_of_fishes_crossed_the_sea'].append(None)
    simulation_output['fishes'].append(None)
    return winner, simulation_output