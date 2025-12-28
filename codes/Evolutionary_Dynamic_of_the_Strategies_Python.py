import axelrod as axl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patheffects as path_effects 

# Basic Strategies
players = [
    axl.Defector(),
    axl.Bully(),
    axl.TitForTat(),
    axl.Alternator(),
    axl.SuspiciousTitForTat(),
    axl.AntiTitForTat(),
    axl.WinStayLoseShift(),
    axl.Cooperator()
]


player_names = ["Defector", "Bully", "TFT", "Alternator", "Suspicious TFT", "Anti TFT", "WSLS", "Cooperator"]

colors = [
    "#0B3C5D",  # Deep Winter Blue - Defector
    "#1C7293",  # Icy Blue - Bully
    "#9B1D20",  # Cranberry Red - Tit For Tat
    "#E63946",  # Bright Red - Alternator
    "#F1FAEE",  # Snow White - Suspicious Tit For Tat
    "#228B22",  # Forest Green - Anti Tit For Tat
    "#006400",  # Dark Green - Win-Stay Lose-Shift 
    "#DAA520",  # Goldenrod - Cooperator
]

# Tournament and Simulation
tournament = axl.Tournament(players, turns=50, repetitions=1)
results = tournament.play()

eco = axl.Ecosystem(results)
eco.reproduce(1000) 
population = eco.population_sizes 

if population is None:
    print("Error: Population data was not generated.")
else:
    sns.set_context("poster", font_scale=1.1)
    
    plt.figure(figsize=(24, 14))

    pop_data = np.array(population).T 
    x_axis = range(len(population)) 

    plt.stackplot(x_axis, pop_data, 
                  labels=player_names, 
                  colors=colors, 
                  edgecolor='black', 
                  linewidth=0.5)

    plt.xscale('log')
    plt.xlim(1, 1000)
    plt.ylim(0, 1)

    initial_pops = pop_data[:, 0]
    cumulative_initial = np.cumsum(initial_pops)
    y_centers_left = cumulative_initial - (initial_pops / 2)

    plt.yticks(y_centers_left, player_names, fontsize=20, fontweight='bold')
    plt.tick_params(axis='y', which='major', pad=10)

    final_pops = pop_data[:, -1]
    cumulative_final = np.cumsum(final_pops)
    y_centers_right = cumulative_final - (final_pops / 2)

    for i, pop_size in enumerate(final_pops):
        percentage = pop_size * 100
        
        if percentage > 1: # For the cooperator, there is a value 0.2, but I use a value greater than 1%

            txt = plt.text(950, y_centers_right[i], f"%{percentage:.1f}", 
                           fontsize=24, fontweight='bold', 
                           color='white',       
                           ha='right',       
                           va='center')
           
    plt.title("Strategy Population Dynamics Based on Average Payoffs", fontsize=30, fontweight='bold', pad=20)
    plt.xlabel("Turn", fontsize=24, labelpad=15)
    
    plt.tight_layout()
    plt.savefig("Evolutionary_Dynamic_of_the_Strategies.png", dpi=300, bbox_inches='tight')

    plt.show()