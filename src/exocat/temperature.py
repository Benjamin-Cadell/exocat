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
        return self.classifications
    
    def plot(self, bins:int=50) -> None:
        """
        Plot the distribution of temperature values with color-coded regions for 'cold', 'warm', and 'hot' categories.

        Parameters
        ----------
        bins : int, optional
            The number of bins to use for the histogram (default is 50).
        """

        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        ax.axvspan(xmin=self.temperature.min(), xmax=273, color='blue', linestyle='--', label='cold', alpha=0.2)
        ax.axvspan(xmin=273, xmax=373, color='orange', linestyle='--', label='warm', alpha=0.2)
        ax.axvspan(xmin=373, xmax=self.temperature.max(), color='red', linestyle='--', label='hot', alpha=0.2)

        ax.hist(self.temperature, bins=bins, color='skyblue', edgecolor='black', align="mid", alpha=0.7)

        cold_mid = (self.temperature.min() + 273) / 2
        warm_mid = (273 + 373) / 2
        hot_mid = (373 + self.temperature.max()) / 2
        y_coord = ax.get_ylim()[1] * 0.9
        ax.text(cold_mid, y_coord, 'Cold', color='blue', fontsize=12, ha='center')
        ax.text(warm_mid, y_coord, 'Warm', color='orange', fontsize=12, ha='center')
        ax.text(hot_mid, y_coord, 'Hot', color='red', fontsize=12, ha='center')

        ax.set_title('Temperature Distribution')
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.5)
        plt.show()
