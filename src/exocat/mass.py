#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Mass:
    """A class to represent and classify mass values."""

    def __init__(self, df: pd.DataFrame|np.ndarray|list) -> None:

        if isinstance(df, pd.DataFrame):
            self.df = df
            self.mass = np.atleast_1d(np.asarray(df["M_b"]))
        else:
            self.df = None
            self.mass = np.atleast_1d(np.asarray(df))

        self.classifications = None

    def classify(self) -> np.ndarray|str:

        output = np.empty_like(self.mass, dtype=object)
        output[self.mass < 0.0007] = "mercury"
        output[(self.mass >= 0.0007) & (self.mass < 0.007)] = "earth"
        output[(self.mass >= 0.007) & (self.mass < 0.07)] = "super earth/subneptune"
        output[(self.mass >= 0.07) & (self.mass < 0.4)] = "neptune"
        output[(self.mass >= 0.4) & (self.mass <= 14)] = "jupiter"
        self.classifications = output
        if self.df is not None:
            self.df["mass_classification"] = self.classifications

        label_colours = {
            "mercury": "brown",
            "earth": "green",
            "super earth/subneptune": "orange",
            "neptune": "blue",
            "jupiter": "red"
        }

        return self.classifications, label_colours

    def plot(self, bins: int = 50) -> None:

        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        # Remove non-positive values because log scale cannot handle them
        mass = self.mass[self.mass > 0]

        xmin = mass.min() * 0.8
        xmax = mass.max() * 1.2

        # Use logarithmic bins
        log_bins = np.logspace(np.log10(xmin), np.log10(xmax), bins)

        ax.axvspan(1e-5, 0.0007, color='brown', label='Mercury', alpha=0.2)
        ax.axvspan(0.0007, 0.007, color='green', label='Earth', alpha=0.2)
        ax.axvspan(0.007, 0.07, color='orange', label='Super Earth/Sub-Neptune', alpha=0.2)
        ax.axvspan(0.07, 0.4, color='blue', label='Neptune', alpha=0.2)
        ax.axvspan(0.4, xmax, color='red', label='Jupiter', alpha=0.2)

        ax.hist(mass, bins=log_bins, color='skyblue', edgecolor='black', alpha=0.7)

        ax.set_xscale("log")
        ax.set_xlim(xmin, xmax)

        # Geometric midpoint for labels on a log axis
        def log_mid(a, b):
            return np.sqrt(a * b)

        y_coord1 = ax.get_ylim()[1] * 0.9
        y_coord2 = ax.get_ylim()[1] * 0.95

        ax.text(log_mid(max(xmin, 1e-5), 0.0007), y_coord1, 'Mercury', color='brown', fontsize=12, ha='center')
        ax.text(log_mid(0.0007, 0.007), y_coord2, 'Earth', color='green', fontsize=12, ha='center')
        ax.text(log_mid(0.007, 0.07), y_coord1, 'Super Earth/Sub-Neptune', color='orange', fontsize=12, ha='center')
        ax.text(log_mid(0.07, 0.4), y_coord2, 'Neptune', color='blue', fontsize=12, ha='center')
        ax.text(log_mid(0.4, xmax), y_coord1, 'Jupiter', color='red', fontsize=12, ha='center')

        ax.set_title('Mass Distribution')
        ax.set_xlabel('Mass (Jupiter Masses)')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.5)

        plt.show()
