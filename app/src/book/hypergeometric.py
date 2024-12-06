# math libs
import numpy as np
from scipy.stats import hypergeom

# flet lib
from flet import BarChart, BarChartGroup, BarChartRod, Page


class HyperGeometricBarChartGroup(BarChartGroup):
    ...


class HyperGeometric:
    def __init__(self, M=1, n=2, N=3):
        super().__init__()
        self._param_M = M
        self._param_n = n
        self._param_N = N
        self.rv = hypergeom(M, n, N)
        self.x = np.arange(0, n + 1)
        self.pmf = self.rv.pmf(self.x)
