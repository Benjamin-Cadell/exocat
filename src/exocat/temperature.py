import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Temperature:
    """A class to represent and classify temperature values."""

    def __init__(self, df: pd.DataFrame|np.ndarray|list) -> None:
        """
        Initialize the Temperature class with a DataFrame or an array of temperature values.
        
        Parameters
        ----------
        df : pd.DataFrame, np.ndarray, or list
            A DataFrame containing a column named 'Teq' or an array/list of temperature values
        """

        if isinstance(df, pd.DataFrame):
            self.df = df
            self.temperature = np.atleast_1d(np.asarray(df["Teq"]))
        else:
            self.df = None
            self.temperature = np.atleast_1d(np.asarray(df))
        
        self.classifications = None

    def classify(self) -> np.ndarray|str:
        """
        Classify the temperature values into categories: 'cold', 'warm', or 'hot'.

        Returns
        -------
        np.ndarray or str
            An array of classifications corresponding to the temperature values.
        """
        
        output = np.empty_like(self.temperature, dtype=object)
        output[self.temperature > 373] = "hot"
        output[(self.temperature <= 373) & (self.temperature > 273)] = "warm"
        output[self.temperature <= 273] = "cold"

        self.classifications = output
        if self.df is not None:
            self.df["temperature_classification"] = self.classifications
        
        label_colours = {
            "cold": "blue",
            "warm": "orange",
            "hot": "red"
        }
        
        return self.classifications, label_colours
    
    def plot(self, bins: int = 50) -> None:

        temperature = self.temperature[np.isfinite(self.temperature)]
        temperature = temperature[temperature > 0]

        if len(temperature) == 0:
            raise ValueError("No positive finite temperature values available for log-scale plotting.")

        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        xmin = temperature.min() * 0.8
        xmax = temperature.max() * 1.2

        log_bins = np.logspace(np.log10(xmin), np.log10(xmax), bins)

        ax.axvspan(max(xmin, 1e-10), min(273, xmax), color='blue', label='cold', alpha=0.2)
        ax.axvspan(max(273, xmin), min(373, xmax), color='orange', label='warm', alpha=0.2)
        ax.axvspan(max(373, xmin), xmax, color='red', label='hot', alpha=0.2)

        ax.hist(temperature, bins=log_bins, color='skyblue', edgecolor='black', alpha=0.7)

        ax.set_xscale("log")
        ax.set_xlim(xmin, xmax)

        def log_mid(a, b):
            return np.sqrt(a * b)

        def add_label(a, b, text, color, y):
            lo = max(a, xmin)
            hi = min(b, xmax)
            if hi > lo:
                ax.text(log_mid(lo, hi), y, text, color=color, fontsize=12, ha='center')

        y_coord = ax.get_ylim()[1] * 0.9

        add_label(xmin, 273, 'Cold', 'blue', y_coord)
        add_label(273, 373, 'Warm', 'orange', y_coord)
        add_label(373, xmax, 'Hot', 'red', y_coord)

        ax.set_title('Temperature Distribution')
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.5)
        ax.legend()

        plt.show()