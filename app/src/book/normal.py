from numpy import linspace
from scipy.stats import norm


class Normal:
    def __init__(self, mu: float = .0, sigma: float = 1.):
        self._mu = mu
        self._sigma = sigma
        self.x = linspace(mu - 3 * sigma, mu + 3 * sigma, 256)
        self.pdf = norm.pdf(self.x, mu, sigma)

    def get_parameters(self):
        return self._mu, self._sigma
