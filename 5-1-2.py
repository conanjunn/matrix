# %%

import numpy as np
import matplotlib.pyplot as plt

# %%
p1 = np.array([1, 1])
p2 = np.array([3, 1])

# %%

# 线上的一个点表示方法：
# p = p1 + t(p2-p1)
# 如果想让p落在p1和p2之间：需满足 0 <= t <= 1

p = p1 + .5*(p2 - p1)
p

# %%


def render():
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='r')
    plt.xticks(np.arange(0, 5, .5))
    plt.yticks(np.arange(0, 5, 0.5))
    plt.show()


plt.scatter([p[0]], p[1])
render()


# %%
# 计算p3在p1,p2线段上的投影点

p3 = np.array([1.5, 2])

plt.scatter([p3[0]], p3[1])
render()


# %%

pJian = p2 - p1
mo = np.linalg.norm(pJian)
n = pJian / mo  # 线段的单位向量

l = (p3 - p1).dot(n)  # 目标点投影到线段上的长度
l

# %%
t = l / mo  # 得到t，即可带入公式p1 + t(p2-p1)

# 上述t的解法可以用这个公式代替，怎么推导出来的不知道。。。
#t = (p3 - p1).dot(pJian) / pJian.dot(pJian)
t
# %%

# 最终结果
ret = p1 + t * (p2 - p1)
ret

# %%
plt.scatter(p3[0], p3[1])
plt.scatter(ret[0], ret[1])
render()

# %%
