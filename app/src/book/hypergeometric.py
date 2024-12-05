# math libs
import numpy as np
from scipy.stats import hypergeom

# flet lib
from flet import BarChart, BarChartGroup, BarChartRod, Page


class HyperGeometricBarChartGroup(BarChartGroup):
    ...


class HyperGeometric(BarChart):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        # self._M = M
        # self._n = n
        # self._N = N
        # self.rv = hypergeom(M, n, N)
        # self.x = np.arange(0, n + 1)
        # self.pmf = self.rv.pmf(self.x)
