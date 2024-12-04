# math libs
import numpy as np
from scipy.stats import hypergeom

# flet lib
from flet import BarChart, BarChartGroup, BarChartRod


class HyperGeometricBarChartGroup(BarChartGroup):
    ...


class HyperGeometric(BarChart):
    def __init__(self, M: int, n: int, N: int):
        """
        :param M: the total number of objects.
        :param n: total number of Type I objects.
        :param N:
        """
        super().__init__()
        self._M = M
        self._n = n
        self._N = N
        self.rv = hypergeom(M, n, N)
        self.x = np.arange(0, n + 1)
        self.pmf = self.rv.pmf(self.x)


