import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math


class Draw:
    def __init__(self, figsize=(10, 5)):
        fig, ax = plt.subplots(figsize=figsize)
        self.ax = ax
        self.fig = fig

    def v(self, v, color='r'):
        self.ax.quiver(v[0], v[1], angles='xy',
                       scale_units='xy', scale=1, color=color)

    def rect(self, m, color='r'):
        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]

        path = Path(m, codes)

        patch = patches.PathPatch(
            path, facecolor='none', edgecolor=color, lw=2)
        self.ax.add_patch(patch)

    def render(self, ticks=[-7, 8]):
        self.ax.axis('scaled')
        self.ax.grid()

        self.ax.set_xticks(np.arange(ticks[0], ticks[1], 1))
        self.ax.set_yticks(np.arange(ticks[0], ticks[1], 1))

        plt.show()


def rectDot(m, rect):
    r = []
    for item in rect:
        r.append(m.dot(item))

    return r
