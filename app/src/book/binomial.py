from scipy.stats import binom
from numpy import arange
import matplotlib.pyplot as plt

class Binomial:
    def __init__(self, n: int = 20, p: float = .5):
        """
        :param n: Number of trials
        :param p: Probability of success on each trial
        """
        self._param_n = n
        self._param_p = p

    def get_parameters(self):
        return self._param_n, self._param_p

    def solve(self, a=None, b=None):
        if b is None:
            b = a
            a = 0

        a, b = int(a), int(b)
        x = arange(0, self._param_n + 1)
        y = binom.pmf(x, self._param_n, self._param_p)

        probabilities = [p for x_val, p in zip(x, y) if a <= x_val <= b]
        total_probability = sum(probabilities)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(x, y, label="Binomial Distribution", color="blue")
        mask = [(val >= a) and (val <= b) for val in x]
        ax.bar(
            [val for val, m in zip(x, mask) if m],
            [y[i] for i, m in enumerate(mask) if m],
            color="skyblue", alpha=0.5, label=f"Sum of probabilities between {a} and {b}"
        )
        ax.axvline(a, color="red", linestyle="--", label=f"x = {a}")
        ax.axvline(b, color="green", linestyle="--", label=f"x = {b}")

        ax.set_title("Binomial Distribution")
        ax.set_xlabel("x")
        ax.set_ylabel("Probability Mass")
        ax.legend()

        total_probability = f'{total_probability:.4f}'
        return total_probability, fig
