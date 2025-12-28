import axelrod as axl
import matplotlib.pyplot as plt
import seaborn as sns

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
# Labels for the heatmap    
labels = [
    "Def",     # Defector
    "Bully",   # Bully
    "TFT",     # Tit For Tat
    "Alt",     # Alternator
    "SusTFT",  # Suspicious Tit For Tat
    "AntiTFT", # Anti Tit For Tat
    "WSLS",    # Win-Stay Lose-Shift
    "Coop"     # Cooperator
]

# Tournament and Simulation
tournament = axl.Tournament(players, turns=50, repetitions=1)
results = tournament.play()

# Heat Map
sns.set_context("poster", font_scale=1.2)

plt.figure(figsize=(12, 10))

ax = sns.heatmap(
    results.payoff_matrix, 
    annot=True,              
    fmt=".2g",               
    xticklabels=labels, 
    yticklabels=labels, 
    cmap='Reds',            
    cbar=False,              
    linewidths=0,           
    square=True, 
    annot_kws={"size": 20, "weight": "normal"} 
)

plt.xticks(rotation=90, ha='right')
plt.yticks(rotation=0)

plt.title("Payoffs", fontsize=24, pad=20, fontweight='bold')

plt.savefig("payoffs.png", dpi=300, bbox_inches='tight')

plt.show()