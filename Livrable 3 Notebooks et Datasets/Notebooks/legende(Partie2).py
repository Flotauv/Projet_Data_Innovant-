import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Création de la figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')  # Suppression des axes

# Élément de la légende
legend_elements = [
    Line2D([0], [0], color='blue', lw=2, linestyle='-', label='Pistes cyclables'),
    Line2D([0], [0], color='red', marker='o', markersize=10, linestyle='', label='Nombre de trajets moyen journalier'),
    Line2D([0], [0], color='gray', marker='o', markersize=10, linestyle='', label='Arceaux vélo'),
    Line2D([0], [0], color='green', lw=2, linestyle='--', label='Contours des communes')
]

# Ajout de la légende
ax.legend(
    handles=legend_elements,
    title="Légende",
    loc="center",
    frameon=False,
    fontsize=10,
    title_fontsize=12
)

# Sauvegarde de l'image

plt.savefig("legende_cyclistes.png", format="png", bbox_inches="tight", dpi=300)
plt.close(fig)

print("L'image a été sauvegardée sous le nom 'legende_cyclistes.png'")
