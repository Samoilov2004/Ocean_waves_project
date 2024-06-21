import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from pyproj import Geod
import module as m

#m.paint_map('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')

#print(m.distance(37.61, 55.75, -99.13, 19.43))

DATA = m.coord_data_like('/Users/mihail/Desktop/Ocean_waves_project/GRD/pacific4min.grd')


print(np.shape(DATA))
DATAN = m.distance_data(DATA, 37.61, 55.75)
print(np.shape(DATAN))

print(DATAN[0])

im = plt.imshow(DATAN, cmap=m.cmap5)
plt.show()
