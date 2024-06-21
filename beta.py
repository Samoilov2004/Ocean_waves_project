import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from pyproj import Geod
import module as m

#m.paint_map('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')

#print(m.distance(37.61, 55.75, -99.13, 19.43))


DATA = m.coord_data_like('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')


print(np.shape(DATA))
DATAN = m.distance_data(DATA, -60, 210)
print(np.shape(DATAN))

print(DATAN[0])



fig, ax = plt.subplots(figsize=(12, 7)) 
im = ax.imshow(DATAN, cmap='cool', extent = [m.give_description('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')[1][i] for i in [2, 3, 0, 1]])
fig.colorbar(im, ax=ax)

plt.show()
