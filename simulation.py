from utils import run_simulation
from parameters import NUMBER_OF_FISHES, WIN_STEPS, STEP

winner, simulation_output = run_simulation(STEP, NUMBER_OF_FISHES, WIN_STEPS)

print(winner)
for key, value in simulation_output.items():
    print(key, value)