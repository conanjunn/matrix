# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
v1 = np.array([1, 5])
v2 = np.array([4, 3])

no1 = np.linalg.norm(v1)  # v1的模
no2 = np.linalg.norm(v2)  # v2的模

print(no1, no2)

# %%


def render():
    plt.plot([0, v1[0]], [0, v1[1]], color='b')
    plt.plot([0, v2[0]], [0, v2[1]], color='g')
    plt.xticks(np.arange(0, 8, 1))
    plt.yticks(np.arange(0, 8, 1))
    plt.axis('equal')
    plt.grid()
    plt.show()


render()

# %%
# 用途一: 计算向量夹角
cos = v1.dot(v2) / (no1 * no2)
cos
# %%
# 反三角函数计算出弧度值
arc = np.arccos(cos)

# %%
# 转为角度
np.degrees(arc)

# %%
# 用途二：计算投影向量

unit1 = v1 / no1
unit2 = v2 / no2


plt.plot([0, unit1[0]], [0, unit1[1]], linewidth=4, color='r')
plt.plot([0, unit2[0]], [0, unit2[1]], linewidth=4, color='r')
render()


# %%
# 算法1：三角函数解法
pro = cos * no1 * unit2
plt.plot([v1[0], pro[0]], [v1[1], pro[1]], color='r')
render()

# %%

pro = cos * no2 * unit1
pro

# %%
plt.plot([v2[0], pro[0]], [v2[1], pro[1]], color='r')
render()

# %%
# 算法2： v2向量点乘v1的单位向量后就是投影向量的模，在乘以单位向量即可得到向量值
pro = v2.dot(unit1) * unit1
plt.plot([v2[0], pro[0]], [v2[1], pro[1]], color='r')
render()

pro = v1.dot(unit2) * unit2
plt.plot([v1[0], pro[0]], [v1[1], pro[1]], color='r')
render()
