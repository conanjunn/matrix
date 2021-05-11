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

v1 = np.array([2, 3])
v2 = np.array([3, 4])
plt.plot([0, v1[0]], [0, v1[1]], color='b')
plt.plot([0, v2[0]], [0, v2[1]], color='b')
render()

# %%
v3 = v2 - v1  # 向量的减法就是把一个线段变成向量
plt.plot([0, v1[0]], [0, v1[1]], color='b')
plt.plot([0, v2[0]], [0, v2[1]], color='b')
plt.plot([0, v3[0]], [0, v3[1]], color='r')  # 向量
plt.plot([v1[0], v2[0]], [v1[1], v2[1]], color='y')  # 原线段
render()
