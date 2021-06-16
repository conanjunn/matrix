# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
v1 = np.array([1, 5])
v2 = np.array([2, 3])

# %%
np.cross(v1, v2)

# %%


def render():
    plt.xticks(np.arange(0, 10, 1))
    plt.yticks(np.arange(0, 10, 1))
    plt.axis('equal')
    plt.grid()
    plt.show()


# %%

"""
法向量
(x, y)的法向量: (y, -x) 或者 (-y, x)
"""
plt.plot([0, v1[0]], [0, v1[1]], color='b')
plt.plot([0, v1[1]], [0, v1[0] * -1], color='r')
plt.plot([0, v1[1] * -1], [0, v1[0]], color='y')
render()
# %%
"""
线段变为向量
"""
v3 = v2 - v1  # 向量的减法就是把一个线段变成向量
plt.plot([0, v1[0]], [0, v1[1]], color='b')
plt.plot([0, v2[0]], [0, v2[1]], color='b')
plt.plot([0, v3[0]], [0, v3[1]], color='r')  # 向量
plt.plot([v1[0], v2[0]], [v1[1], v2[1]], color='y')  # 原线段
render()

# %%
