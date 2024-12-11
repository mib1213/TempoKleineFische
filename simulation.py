from utils import run_simulation
from parameters import NUMBER_OF_FISHES, WIN_STEPS, STEP

winner, simulation_output = run_simulation(STEP, NUMBER_OF_FISHES, WIN_STEPS)

for i in range(len(simulation_output['counter'])):
    print("===============================", "<br>")
    for key, value in simulation_output.items():
        print(f"{key} = {value[i]} <br>")