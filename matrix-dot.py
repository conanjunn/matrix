# %%
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

# %%

m1 = np.array([
    [0, -1],
    [1, 0]
])

m2 = np.array([
    [1, 1],
    [0, 1]
])

# %%


def renderV(v, color='k'):
    fig, ax = plt.subplots()
    a = ax.quiver(0, 0, v[0], v[1], angles='xy',
                  scale_units='xy', scale=1, color=color)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    plt.grid()  # 生成网格
    plt.show()


v = np.array([3, 4])

renderV(v)

# %%
# 先进行第一次变换
tran1 = m1.dot(v)
renderV(tran1)
# %%
# 用第一次的变换结果进行第二次变换得到结果
tran2 = m2.dot(tran1)
renderV(tran2)

# %%
# 矩阵乘法就是将两次变换合并。
# 注意需要用第二次乘第一次（效仿函数从右往左）
mm = m2.dot(m1)
tran3 = mm.dot(v)
renderV(tran3)
