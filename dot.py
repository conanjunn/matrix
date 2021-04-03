# %%
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


# %%
m1 = np.array([[1, 1], [2, 2]])
m1

# %%
m2 = np.array([[3, 3], [4, 4]])
m2.T

# %%
m1.dot(m2)

# %%
m3 = np.array([[1, 1], [2, 2], [3, 3]])
m3

# %%
m3.shape

# %%
m4 = np.array([[1, 1, 1], [2, 2, 2]])
m4.shape

# %%
m3.dot(m4)

# %%
# 三角形
triangle = np.array([[0, 0, 1], [3, 3, 1], [3, 0, 1]])
triangle

# %%
triangle[:, :2]

# %%


def render(m, color):
    fig, ax = plt.subplots()
    ax.add_patch(Polygon(m, color=color))

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    plt.show()


# %%
render(triangle[:, :2], 'r')

# %%
# 矩阵平移
a = 1
b = 1
m = triangle.dot(np.array([[1, 0, 0], [0, 1, 0], [a, b, 1]]))
m

# %%
render(m[:, :2], 'b')

# %%
