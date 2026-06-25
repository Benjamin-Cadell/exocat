#%%
import requests
from astropy.io import ascii

link = "https://www.astro.keele.ac.uk/jkt/tepcat/allinfo-ascii.txt"

txt = requests.get(link).text

lines = txt.splitlines()
# Strip the leading comment marker from the header line
lines[0] = lines[0].removeprefix("#").strip()

ascii_dat = ascii.read(
    lines,
    format="fixed_width",
    delimiter=" ",
    comment=None,
)

dat = ascii_dat.to_pandas()
# Strip leading and trailing hyphens from column names
dat.columns = dat.columns.str.strip("-")
