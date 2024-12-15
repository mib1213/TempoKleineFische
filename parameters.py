NUMBER_OF_FISHES = 4 # can be added of one's choice
NUMBER_OF_SIMULATIONS = 100000 # for testing probabilities, applicable in main.py
STEP = -5 # the difference between the boat and the fish 
# Step range can be set up manually where you want to test the probability, since we are interested in 
# the equal probabilty, it must be in the range between around -4 to -7 but just out of curiosity we
# are testing from -1 to -10.
STEP_RANGE_START = -10
STEP_RANGE_END = -1
WIN_STEPS = 5 # number of steps after which the fishes will reach the sea
RANDOM_STATE = 42