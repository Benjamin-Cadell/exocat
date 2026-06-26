import exocat
import numpy as np

def test_e2e():

    df = exocat.tepcat_csv()
    df = exocat.tepcat_tidy(df)
    m = exocat.Mass(df)
    _, ml = m.classify()
    m.plot()
    t = exocat.Temperature(df)
    _, tl = t.classify()
    t.plot()
    d = exocat.BulkDensity(df)
    d.plot()
    _, dl = d.classify()

    plot = exocat.Plot(df)
    plot.plot_cmap(
        x="Period(day)",
        y="Teq",
        c="density_classification",
        clabels=dl,
        cmap="viridis",
        title="")