def check_for_winner(number_of_fishes_caught_by_the_boat, 
                    number_of_fishes_crossed_the_sea, 
                    number_of_fishes):
    half_of_number_of_fishes = number_of_fishes // 2 
    if number_of_fishes_caught_by_the_boat == half_of_number_of_fishes and number_of_fishes_crossed_the_sea == half_of_number_of_fishes:
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
                       fish_steps_list,
                       caught_by_fisher_list,
                       have_crossed_the_sea_list,
                       win_steps):
    for i, (caught_by_fisher, have_crossed_the_sea) in enumerate(zip(caught_by_fisher_list, have_crossed_the_sea_list)):
        if dice == i:
            if not caught_by_fisher:
                if not have_crossed_the_sea:
                    fish_steps_list[i] += 1
                    if fish_steps_list[i] == win_steps:
                        have_crossed_the_sea_list[i] = 1
                        number_of_fishes_crossed_the_sea += 1
                else:
                    for j, (caught_by_fisher_inner, have_crossed_the_sea_inner) in enumerate(zip(caught_by_fisher_list, have_crossed_the_sea_list)):
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