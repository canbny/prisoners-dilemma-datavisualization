import axelrod as axl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

strategies = [
    axl.Defector(),
    axl.Bully(),
    axl.TitForTat(),
    axl.Alternator(),
    axl.SuspiciousTitForTat(),
    axl.AntiTitForTat(),
    axl.WinStayLoseShift(),
    axl.Cooperator()
]

labels = ["Defector", "Bully", "TFT", "Alternator", "SusTFT", "AntiTFT", "WSLS", "Cooperator"]

tournament = axl.Tournament(strategies, turns=200, repetitions=100)
results = tournament.play()

plot_data = []
for i, player_obj in enumerate(strategies):
    strat_name = labels[i]
    for j, opponent_obj in enumerate(strategies):
        scores_i = results.payoffs[i][j]
        scores_j = results.payoffs[j][i]
        diffs = [si - sj for si, sj in zip(scores_i, scores_j)]
        for diff in diffs:
            plot_data.append({
                'Strategy': strat_name,
                'Payoff Difference': diff
            })

df = pd.DataFrame(plot_data)

sns.set_context("poster", font_scale=1.2) 
sns.set_style("whitegrid")

plt.figure(figsize=(20, 10))

edge_color = "#800020" 

sns.violinplot(
    data=df,
    x='Strategy',
    y='Payoff Difference',
    color="#ffb6c1", 
    inner="quart",
    linewidth=1.5,       
    scale='width',
    cut=0,
    edgecolor=edge_color 
)

means = df.groupby('Strategy', sort=False)['Payoff Difference'].mean()
x_range = range(len(strategies))

plt.hlines(
    y=means, 
    xmin=[x - 0.3 for x in x_range], 
    xmax=[x + 0.3 for x in x_range], 
    color='#D62728', 
    lw=5,            
    zorder=10,
    label='Mean Difference'
)

plt.title("Distribution of Payoff Differences per Stage Game", fontsize=32, fontweight='bold', pad=30)

plt.xlabel("", fontsize=24, labelpad=20) 

plt.ylabel("", fontsize=24, labelpad=20)

plt.grid(axis='y', linestyle='--', alpha=0.6, linewidth=1.5)
plt.xticks(fontsize=20, rotation=0)
plt.ylim(-6, 6)
plt.yticks(fontsize=20)


plt.tight_layout()

plt.savefig("violin_plot.png", dpi=300, bbox_inches='tight')

plt.savefig("violin_plot.pdf", format='pdf', bbox_inches='tight')

plt.show()