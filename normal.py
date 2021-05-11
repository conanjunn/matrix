# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
v1 = np.array([2, 3])

# %%


def render():
    plt.xticks(np.arange(0, 8, 1))
    plt.yticks(np.arange(0, 8, 1))
    plt.axis('equal')
    plt.grid()
    plt.show()


# %%
plt.plot([0, v1[0]], [0, v1[1]], color='b')
plt.plot([0, v1[1]], [0, v1[0] * -1], color='r')
plt.plot([0, v1[1] * -1], [0, v1[0]], color='r')
render()

# %%
