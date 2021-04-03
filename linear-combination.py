# %%
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

# %%


def renderV(v, color='k'):
    fig, ax = plt.subplots()
    a = ax.quiver(0, 0, v[0], v[1], angles='xy',
                  scale_units='xy', scale=1, color=color)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    plt.grid()  # 生成网格
    plt.show()


# %%

# 空间中的基向量
base = np.array([
    [1, 0],
    [0, 1]
])
renderV(base[0], 'b')
renderV(base[1], 'r')

# %%

# 用基向量可以生成此空间中的其他所有向量
target = np.array([3, 4])
v = base.dot(target)
renderV(v)

# %%
# 拆解分析矩阵和向量的点乘
x = 3
y = 4
# %%
# 第一步对应轴先做数乘
X = x * base[0]
renderV(X)
# %%
Y = y * base[1]
renderV(Y)
# %%
# 第二步：将两个数乘的结果做加法,即可得到结果
V = X + Y
renderV(V)
# %%
# 可以通过改变基向量来实现线性变换
base2 = np.array([
    [1, 0],
    [0, -1]
])
renderV(base2[0], 'b')
renderV(base2[1], 'r')
# %%
# target无需改变，只需和不同的基向量相乘即可实现它的线性变换
v = base2.dot(target)
renderV(v)
