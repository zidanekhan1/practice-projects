import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure with grey background
fig, ax = plt.subplots(figsize=(6, 4))
fig.patch.set_facecolor("lightgrey")   # background of figure
ax.set_facecolor("lightgrey")          # background of axes

# Draw white stripe
ax.add_patch(patches.Rectangle((0, 2/3), 1, 1/3, color="white"))

# Draw blue stripe
ax.add_patch(patches.Rectangle((0, 1/3), 1, 1/3, color="blue"))

# Draw red stripe
ax.add_patch(patches.Rectangle((0, 0), 1, 1/3, color="red"))

# Formatting
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.show()
