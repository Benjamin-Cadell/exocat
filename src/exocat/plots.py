import matplotlib.pyplot as plt
import numpy as np

class Plot:
    """A class to create scatter plots with color mapping based on a DataFrame."""

    def __init__(self, df: np.ndarray) -> None:
        """
        Initialize the Plot class with a DataFrame.

        Parameters
        ----------
        df : np.ndarray
            A DataFrame containing the data to be plotted.
        """

        self.df = df
    
    def plot_cmap(self, x:str, y:str, c:str, cmap:str='viridis', title:str=None) -> None:
        """
        Create a scatter plot with color mapping based on a DataFrame.
        
        Parameters
        ----------
        x : str
            The column name for the x-axis values.
        y : str
            The column name for the y-axis values.
        c : str
            The column name for the color mapping values.
        cmap : str, optional
            The colormap to use for the scatter plot (default is 'viridis').
        title : str, optional
            The title of the plot (default is None).

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(self.df[x], self.df[y], c=self.df[c], cmap=cmap)
        plt.colorbar(scatter, label=c)
        plt.xlabel(x)
        plt.ylabel(y)
        if title:
            plt.title(title)
        plt.grid()
        plt.show()