# %%
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

# %%
m = np.array([
    [1, 0],
    [0, 1]
])

v = np.array([1, 0])

m.dot(v)

# %%


def renderV(v, color='k'):
    fig, ax = plt.subplots()
    a = ax.quiver(0, 0, v[0], v[1], angles='xy',
                  scale_units='xy', scale=1, color=color)
    ax.set_xlim([-5, 8])
    ax.set_ylim([-5, 8])

    plt.grid()  # 生成网格
    plt.show()


# %%
renderV(v)
# %%
m2 = np.array([
    [np.cos(30*np.pi/180), -1 * np.sin(30*np.pi/180)],
    [np.sin(30*np.pi/180), np.cos(30*np.pi/180)]
])
v2 = m2.dot(np.array([1, 0]))
v2
# %%
renderV(v2)

# %%
