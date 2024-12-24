from numpy import linspace, inf
from scipy.stats import norm
import matplotlib.pyplot as plt
from io import BytesIO


class Normal:
    def __init__(self, mu: float = .0, sigma: float = 1.):
        self._param_mu = mu
        self._param_sigma = sigma

    def get_parameters(self):
        return self._param_mu, self._param_sigma

    def solve(self, a=None, b=None):
        if b is None:
            b = a
            a = -inf
        a = float(a)
        b = float(b)
        x = linspace(self._param_mu - 3 * self._param_sigma, self._param_mu + 3 * self._param_sigma, 512)  # Generate x values from -4 to 4
        y = norm.pdf(x, self._param_mu, self._param_sigma)  # Standard normal PDF (mean=0, stddev=1)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label="Standard Normal Distribution", color="blue")
        ax.fill_between(
            x, y, 0, where=(x >= a) & (x <= b), color="skyblue", alpha=0.5, label=f"Area between {a} and {b}"
        )
        ax.axvline(a, color="red", linestyle="--", label=f"x = {a}")
        ax.axvline(b, color="green", linestyle="--", label=f"x = {b}")

        ax.set_title("Standard Normal Distribution")
        ax.set_xlabel("x")
        ax.set_ylabel("Probability Density")
        ax.legend()

        # Save the plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close(fig)  # Close the figure to avoid memory leaks
        area = norm.cdf(b, 0, 1) - norm.cdf(a, 0, 1)
        area = f'{area:.4f}'
        return area, fig
