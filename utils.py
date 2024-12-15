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
                       caught_by_the_boat_list: list[bool]) -> boat_return:
    boat_steps += 1
    number_of_fishes_caught_by_the_boat: int = 0
    # number of fishes caught by the boat variable needs to be set to 0 everytime this function
    # is called, the reason being the for loop below calculates the TOTAL number of fishes caught
    # by the boat everytime, so even if there were fishes caught before, the below for loop will 
    # count them again.
    for i, fish_steps in enumerate(fish_steps_list):
        if boat_steps >= fish_steps:
            caught_by_the_boat_list[i] = 1
            number_of_fishes_caught_by_the_boat += 1
    return (boat_steps, 
            number_of_fishes_caught_by_the_boat, 
            caught_by_the_boat_list)

fish_return: TypeAlias = tuple[int, int, int, list[int], list[bool], list[bool]]

def fish_moves_forward(dice: int,
                       boat_steps: int,
                       number_of_fishes_caught_by_the_boat: int,
                       number_of_fishes_crossed_the_sea: int,
                       win_steps: int, 
                       fish_steps: list[int],
                       caught_by_the_boat_list: list[bool],
                       crossed_the_sea_list: list[bool]) -> fish_return:
    # dice corresponds to fish index
    if not caught_by_the_boat_list[dice]:
        if not crossed_the_sea_list[dice]:
            fish_steps[dice] += 1
            # everytime step increases, check if that fish has also crossed the sea
            if fish_steps[dice] == win_steps:
                crossed_the_sea_list[dice] = 1
                number_of_fishes_crossed_the_sea += 1
        else: # in case if the fish had already crossed the sea but still got its index
              # so any fish in its place can step

            # make sure that this iterator is being used only in 1 for loop, otherwise it would
            # be "partially consumed", in this particular case it should be okay because whenever
            # we are repeating the simulation, we are initiating a fresh iterator in every iteration
            iterator: iter = iter(zip(caught_by_the_boat_list, crossed_the_sea_list))

            # As a strategy that should be used by fishes in order to have higher chances of winning
            # is to always move a fish that is closer to the sea when given a chance to move any fish,
            # so I am findind a fish that has the closest distance to the sea through this for-loop
            # and saving the results in the 'differences' dictionary.
            differences: dict[int: int] = {}
            for i, (caught_by_the_boat, crossed_the_sea) in enumerate(iterator):
                # only fishes that are NOT caught by the boat and also NOT have crossed the sea (which
                # would also mean the fish that has the original dice number is excluded) should be
                # added to the 'differences' dict.
                if not caught_by_the_boat and not crossed_the_sea:
                    differences[i] = win_steps - fish_steps[i]
            # find the key (fish number) that has the minimum value
            fish_to_move: int = min(differences, key=differences.get)
            fish_steps[fish_to_move] += 1
            if fish_steps[fish_to_move] == win_steps:
                crossed_the_sea_list[fish_to_move] = 1
                number_of_fishes_crossed_the_sea += 1

    else: # in case if the corresponding fish had already caught by the boat
          # the boat gets to move
        boat_move_return: boat_return = boat_moves_forward(boat_steps, 
                                                           fish_steps,
                                                           caught_by_the_boat_list)
        boat_steps: int = boat_move_return[0]
        number_of_fishes_caught_by_the_boat: int = boat_move_return[1]
        caught_by_the_boat_list: list[bool] = boat_move_return[2]

    return (boat_steps, 
            number_of_fishes_caught_by_the_boat,
            number_of_fishes_crossed_the_sea,
            fish_steps,
            caught_by_the_boat_list,
            crossed_the_sea_list)

simulation: TypeAlias = dict[str: list[int | tuple[int] | tuple[bool]]]
simulation_return: TypeAlias = tuple[str, simulation]

def run_simulation(step: int, 
                   number_of_fishes: int, 
                   win_steps: int, 
                   random_state: int = None) -> simulation_return:
    # initiating a list with 0s of the size equal to "number_of_fishes"
    initial_values: list[int] = [0] * number_of_fishes

    fish_steps: list[int] = initial_values[:]
    caught_by_the_boat: list[bool] = initial_values[:]
    crossed_the_sea: list[bool] = initial_values[:]
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
                                     'caught_by_the_boat': [],
                                     'crossed_the_sea': []}
    # one game simulation inside this while loop
    while True:
        simulation_output['counter'].append(counter)
        winner: str | None = check_for_winner(number_of_fishes_caught_by_the_boat, 
                                              number_of_fishes_crossed_the_sea, 
                                              number_of_fishes=number_of_fishes)
        simulation_output['winner'].append(winner)

        if winner:  # once we get any value except None from the "check_for_winner" function,
                    # we don't need to run this loop anymore
            break
        if random_state: # if the user has provided a random seed
            random.seed(random_state)
            # random_state needs to be updated for every iteration otherwise we will get the same
            # dice number in every iteration
            random_state += counter
            # we are incrementing counter to update its seed and not just +1, because it is
            # less prone to similar values generation in case of multiple simulations
        
        # beware: here this +1 is not the same in range function, this +1 is because we need 2 more
        # dice options as number of fishes, also not +2 because randint() function includes both
        # boundaries.
        dice: int = random.randint(0, number_of_fishes + 1)
        
        if dice == number_of_fishes or dice == number_of_fishes + 1:
            boat_move_return: boat_return = boat_moves_forward(boat_steps, 
                                                               fish_steps,
                                                               caught_by_the_boat)
            boat_steps: int = boat_move_return[0]
            number_of_fishes_caught_by_the_boat: int = boat_move_return[1]
            caught_by_the_boat: list[bool] = boat_move_return[2]                          
        else:
            fishes_move_return: fish_return = fish_moves_forward(dice,
                                                                 boat_steps,
                                                                 number_of_fishes_caught_by_the_boat,
                                                                 number_of_fishes_crossed_the_sea,
                                                                 win_steps,
                                                                 fish_steps,
                                                                 caught_by_the_boat,
                                                                 crossed_the_sea)
            boat_steps: int = fishes_move_return[0]
            number_of_fishes_caught_by_the_boat: int = fishes_move_return[1]
            number_of_fishes_crossed_the_sea: int = fishes_move_return[2]
            fish_steps: list[int] = fishes_move_return[3]
            caught_by_the_boat: list[bool] = fishes_move_return[4]
            crossed_the_sea: list[bool] = fishes_move_return[5]

        counter += 1
        simulation_output['dice'].append(dice)
        simulation_output['boat_steps'].append(boat_steps)
        simulation_output['number_of_fishes_caught_by_the_boat'].append(number_of_fishes_caught_by_the_boat)
        simulation_output['number_of_fishes_crossed_the_sea'].append(number_of_fishes_crossed_the_sea)
        # below 3 values have to be appended as a Tuple and NOT as a list, the reason being when we
        # append any 'mutable' object like list, dict, set, etc to a list, it actually appends just a
        # shollow copy of it, meaning only its reference, but the main address in the memory remains
        # the same, so if that 'mutable' object' is changed later on, the values here will also be 
        # changed. In this concrete example, it would mean that my simulation_output-fish_steps list 
        # will only be showing the last entry of the list and all the previous history will be updated 
        # to the last entry which ofcourse we don't want here, so an easy solution would be to convert
        # the list into a Tuple before appending, and as they are immutable we can be sure that they
        # won't get updated later on, another solution would be to use copy.deepcopy() function,
        # and still use the list, but in that case the program is relatively slower so I preferred
        # Tuple conversion.
        simulation_output['fish_steps'].append(tuple(fish_steps))
        simulation_output['caught_by_the_boat'].append(tuple(caught_by_the_boat))
        simulation_output['crossed_the_sea'].append(tuple(crossed_the_sea))

    # need to append one None value at the end of each list except to "winner" and "counter",
    # the reason being the while loop is terminated as soon as it gets the winner value but until
    # that time it had already appended the winner value and counter value to the simulation output
    # which means we would get unequal sizes for lists in values in simulation output, specifically
    # speaking one less value in other lists, so I am appending one None everywhere where the length
    # is less than the length of the counter or dice list.
    len_counter: int = len(simulation_output['counter'])
    for key in simulation_output.keys():     
        if len(simulation_output[key]) < len_counter:
            simulation_output[key].append(None)

    return winner, simulation_output