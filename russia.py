import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(6, 4))
fig.patch.set_facecolor("lightgrey")   
ax.set_facecolor("lightgrey")         

ax.add_patch(patches.Rectangle((0, 2/3), 1, 1/3, color="white"))

ax.add_patch(patches.Rectangle((0, 1/3), 1, 1/3, color="blue"))

ax.add_patch(patches.Rectangle((0, 0), 1, 1/3, color="red"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.show()

