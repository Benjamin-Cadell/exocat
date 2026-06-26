import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize, LogNorm

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
    
    def plot_cmap(self, x:str, y:str, c:str,
                  cmap:str='viridis',
                  title:str=None,
                  xscale:str='log',
                  yscale:str='log',
                  cscale:str='log',
                  clabels:dict=None,
    ) -> None:
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
        clabels : dict, optional
            A dictionary with labels and colours to draw from the df (default is None).
        cmap : str, optional
            The colormap to use for the scatter plot (default is 'viridis').
        title : str, optional
            The title of the plot (default is None).

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))

        if clabels is not None:
            c = [clabels[label] for label in self.df[c]]
            norm = None
        else:
            cmap = plt.get_cmap(cmap)
            if cscale == "log":
                norm = LogNorm(
                    vmin=self.df[c][self.df[c] > 0].min(),
                    vmax=self.df[c].max()
                )
            else:
                norm = Normalize(
                    vmin=self.df[c].min(),
                    vmax=self.df[c].max()
                )
                c = self.df[c]

        scatter = plt.scatter(
            self.df[x],
            self.df[y],
            c=c,
            cmap=cmap,
            norm=norm,
        )
        if clabels is None:
            plt.colorbar(scatter, label=c)
        else:
            for label, color in clabels.items():
                plt.scatter([], [], c=color, label=label)
            plt.legend()
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xscale(xscale)
        plt.yscale(yscale)
        if title:
            plt.title(title)
        plt.grid()
        plt.show()