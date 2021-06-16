
# %%
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math


# %%

def render(vertex):
    fig, ax = plt.subplots()

    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]

    path = Path(vertex, codes)

    patch = patches.PathPatch(path, facecolor='none', edgecolor='r', lw=2)
    ax.add_patch(patch)
    ax.axis('scaled')
    ax.grid()

    ax.set_xticks(np.arange(-3, 6, 1))
    ax.set_yticks(np.arange(-3, 6, 1))

    plt.show()


# %%

verts = np.array([
    [0, 0],  # left, bottom
    [2, 0],  # left, top
    [2, 1],  # right, top
    [0, 1],  # right, bottom
    [0, 0],  # ignored
])

render(verts)

# %%
rotate = np.array([
    [math.cos(math.pi / 180 * 30), math.sin(math.pi / 180 * 30) * -1],
    [math.sin(math.pi / 180 * 30), math.cos(math.pi / 180 * 30)]
])
rotate

# %%

newVerts = []
for index, item in enumerate(verts):
    newVerts.append(rotate.dot(item))

newVerts

# %%
render(newVerts)

# %%
np.linalg.inv(rotate)

# %%
ax.quiver(2, 2, angles='xy', scale_units='xy', scale=1, color="r")
