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

        return self.classifications

    def plot(self, bins:int=50) -> None:

        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        ax.axvspan(xmin=-999, xmax=0.5, color='green', linestyle='--', label='gaseous', alpha=0.2)
        ax.axvspan(xmin=0.5, xmax=2, color='blue', linestyle='--', label='gaseous/water-rich', alpha=0.2)
        ax.axvspan(xmin=2, xmax=7, color='orange', linestyle='--', label='rocky', alpha=0.2)
        ax.axvspan(xmin=7, xmax=13, color='red', linestyle='--', label='metallic', alpha=0.2)
        ax.axvspan(xmin=13, xmax=999, color='purple', linestyle='--', label='super dense', alpha=0.2)

        ax.hist(self.density, bins=bins, color='skyblue', edgecolor='black', align="mid", alpha=0.7)

        xmin = np.min(self.density) - 1
        xmax = np.max(self.density) + 1

        gas_mid = (xmin + 0.5) / 2
        water_mid = (0.5 + 2) / 2
        rocky_mid = (2 + 7) / 2
        metallic_mid = (7 + 13) / 2
        super_dense_mid = (13 + xmax) / 2
        y_coord1 = ax.get_ylim()[1] * 0.9
        y_coord2 = ax.get_ylim()[1] * 0.95
        ax.text(gas_mid, y_coord1, 'Gaseous', color='green', fontsize=12, ha='center')
        ax.text(water_mid, y_coord2, 'Gaseous/Water-Rich', color='blue', fontsize=12, ha='center')
        ax.text(rocky_mid, y_coord1, 'Rocky', color='orange', fontsize=12, ha='center')
        ax.text(metallic_mid, y_coord2, 'Metallic', color='red', fontsize=12, ha='center')
        ax.text(super_dense_mid, y_coord1, 'Super Dense', color='purple', fontsize=12, ha='center')

        ax.set_xlim(xmin, xmax)
        ax.set_title('Bulk Density Distribution')
        ax.set_xlabel('Bulk Density (kg/m³)')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.5)
        plt.show()
