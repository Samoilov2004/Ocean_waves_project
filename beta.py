import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from pyproj import Geod
import module_ref as mf
import modele as m

m.paint_map('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')

print(m.distance(55.75, 37.61, 19.43, -99.13))


DATA = m.coord_data_like('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')



DATAN = m.distance_data(DATA, 0, 200)






fig, ax = plt.subplots(figsize=(12, 7)) 
im = ax.imshow(DATAN, cmap='cool', extent = [m.get_description('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')[1][i] for i in [2, 3, 0, 1]])
fig.colorbar(im, ax=ax)

plt.show()
"""

chij = '/Users/mihail/Desktop/Ocean_waves_project/GRD/chij.grd'

DATA = m.triangle_time(chij, 27, 142)
m.paint(DATA)
"""