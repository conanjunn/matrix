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
    # ax.set_xlim([-5, 5])
    # ax.set_ylim([-5, 5])
    plt.xticks(np.arange(-3, 3, 1))
    plt.yticks(np.arange(-3, 3, 1))

    plt.grid()  # 生成网格
    plt.show()


# %%

# 在标准坐标系（下文简称：A空间）中的x基向量
renderV(v)

# %%
m2 = np.array([
    [np.cos(30*np.pi/180), -1 * np.sin(30*np.pi/180)],
    [np.sin(30*np.pi/180), np.cos(30*np.pi/180)]
])
v2 = m2.dot(v)
v2

# %%

# 将A空间进行了一次变换，我们起名叫：B空间
# B空间里的x基向量在A空间坐标系里的展示
renderV(v2)

# 在B空间v是[1,0],而在A空间v是[0.8, 0.5]
# 所以这里可以理解为：m2是个翻译器，将B空间向量，翻译为用A空间的坐标表示，让A空间可以明白，B空间的向量该如何在自己的坐标系里表示

# %%

# 问题：现在给一个A空间的向量v，请问怎么用B空间的坐标系去描述它？

# 只需将m2取逆矩阵
m3 = np.linalg.inv(m2)
m3

# %%
# 然后再点乘v向量，即可得出
v3 = m3.dot(v)
v3

# %%
renderV(v3)
