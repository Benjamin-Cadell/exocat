#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class BulkDensity:
    """A class to represent and classify bulk density values."""

    def __init__(self, df: pd.DataFrame|np.ndarray|list) -> None:

        if isinstance(df, pd.DataFrame):
            self.df = df
            self.density = np.atleast_1d(np.asarray(df["rho_b"]))
        else:
            self.df = None
            self.density = np.atleast_1d(np.asarray(df))

        self.classifications = None

    def classify(self) -> np.ndarray|str:

        density_jup = 1.326
        density_gcm3 = self.density * density_jup
        
        output = np.empty_like(density_gcm3, dtype=object)
        output[density_gcm3 < 0.5] = "gaseous"
        output[(density_gcm3 >= 0.5) & (density_gcm3 < 2)] = "gaseous/water-rich"
        output[(density_gcm3 >= 2) & (density_gcm3 < 7)] = "rocky"
        output[(density_gcm3 >= 7) & (density_gcm3 < 13)] = "metallic"
        output[density_gcm3 >= 13] = "super dense"
        self.classifications = output
        if self.df is not None:
            self.df["density_classification"] = self.classifications

        label_colours = {
            "gaseous": "green",
            "gaseous/water-rich": "blue",
            "rocky": "orange",
            "metallic": "red",
            "super dense": "purple"
        }

        return self.classifications, label_colours

    def plot(self, bins: int = 50) -> None:

        density_jup = 1.326
        density_gcm3 = self.density * density_jup

        density_gcm3 = density_gcm3[np.isfinite(density_gcm3)]
        density_gcm3 = density_gcm3[density_gcm3 > 0]

        if len(density_gcm3) == 0:
            raise ValueError("No positive finite density values available for log-scale plotting.")

        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        xmin = density_gcm3.min() * 0.8
        xmax = density_gcm3.max() * 1.2

        log_bins = np.logspace(np.log10(xmin), np.log10(xmax), bins)

        ax.axvspan(max(xmin, 1e-10), min(0.5, xmax), color='green', label='gaseous', alpha=0.2)
        ax.axvspan(max(0.5, xmin), min(2, xmax), color='blue', label='gaseous/water-rich', alpha=0.2)
        ax.axvspan(max(2, xmin), min(7, xmax), color='orange', label='rocky', alpha=0.2)
        ax.axvspan(max(7, xmin), min(13, xmax), color='red', label='metallic', alpha=0.2)
        ax.axvspan(max(13, xmin), xmax, color='purple', label='super dense', alpha=0.2)

        ax.hist(density_gcm3, bins=log_bins, color='skyblue', edgecolor='black', alpha=0.7)

        ax.set_xscale("log")
        ax.set_xlim(xmin, xmax)

        def log_mid(a, b):
            return np.sqrt(a * b)

        def add_label(a, b, text, color, y):
            lo = max(a, xmin)
            hi = min(b, xmax)
            if hi > lo:
                ax.text(log_mid(lo, hi), y, text, color=color, fontsize=12, ha='center')

        y_coord1 = ax.get_ylim()[1] * 0.9
        y_coord2 = ax.get_ylim()[1] * 0.95

        add_label(xmin, 0.5, 'Gaseous', 'green', y_coord1)
        add_label(0.5, 2, 'Gaseous/Water-Rich', 'blue', y_coord2)
        add_label(2, 7, 'Rocky', 'orange', y_coord1)
        add_label(7, 13, 'Metallic', 'red', y_coord2)
        add_label(13, xmax, 'Super Dense', 'purple', y_coord1)

        ax.set_title('Bulk Density Distribution')
        ax.set_xlabel('Bulk Density (g/cm³)')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.5)
        ax.legend()

        plt.show()