from scipy.stats import hypergeom
import matplotlib.pyplot as plt


class HyperGeometric:
    def __init__(self, M: int=60, n: int=10, N: int=20):
        """
        :param M: Total number of objects
        :param n: Number of success states in the population
        :param N: Number of draws
        """
        self._param_M = M
        self._param_n = n
        self._param_N = N

    def get_parameters(self):
        return self._param_M, self._param_n, self._param_N

    def solve(self, a=None, b=None):
        if b is None:
            b = a
            a = 0  # Minimum possible value for HyperGeometric distribution

        a, b = int(a), int(b)
        x = range(max(0, self._param_N - (self._param_M - self._param_n)), min(self._param_N, self._param_n) + 1)
        y = hypergeom.pmf(x, self._param_M, self._param_n, self._param_N)

        # Calculate the sum of probabilities (discrete equivalent of area)
        probabilities = [p for x_val, p in zip(x, y) if a <= x_val <= b]
        total_probability = sum(probabilities)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(x, y, label="HyperGeometric Distribution", color="blue")
        mask = [(val >= a) and (val <= b) for val in x]
        ax.bar(
            [val for val, m in zip(x, mask) if m],
            [y[i] for i, m in enumerate(mask) if m],
            color="skyblue", alpha=0.5, label=f"Sum of probabilities between {a} and {b}"
        )
        ax.axvline(a, color="red", linestyle="--", label=f"x = {a}")
        ax.axvline(b, color="green", linestyle="--", label=f"x = {b}")

        ax.set_title("HyperGeometric Distribution")
        ax.set_xlabel("x")
        ax.set_ylabel("Probability Mass")
        ax.legend()

        plt.close(fig)

        total_probability = f'{total_probability:.4f}'
        return total_probability, fig
