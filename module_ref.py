import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from pyproj import Geod

#переписать

def cmap5():
    negative_colors = [(0.0, 'navy'), (0.5, 'skyblue'), (1.0, 'white')]
    negative_cmap = LSC.from_list('negative', negative_colors)

    positive_colors = [(0.0, 'limegreen'), (1.0, 'darkgreen')]
    positive_cmap = LSC.from_list('positive', positive_colors)

    colors = np.vstack((negative_cmap(np.linspace(0, 1, 256)), positive_cmap(np.linspace(0, 1, 256))))
    my_cmap = LSC.from_list('my_cmap', colors)
    return my_cmap
cmap5 = cmap5()


class GRD_file():
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            f.readline()  # Пропуск первой строки (DSAA)

            self.cols, self.rows = map(int, f.readline().split())
            self.lon_min, self.lon_max = map(float, f.readline().split())
            self.lat_min, self.lat_max = map(float, f.readline().split())
            self.min_depth, self.max_depth = map(float, f.readline().split())

            data = [float(value) for value in f.read().split()]
            data = np.array(data).reshape(self.rows, self.cols)
            self.data = np.flip(data, axis=0)  # дело в том что в файле строки снизу вверх идут и поэтому так пишем

    def paint_map(self, cmap='viridis', vmin=None, vmax=None):
        limits = [self.lon_min, self.lon_max, self.lat_min, self.lat_max]
        max_dep = self.data.max()
        fig, ax = plt.subplots(figsize=(12, 7))
        im = ax.imshow(self.data, cmap=cmap5, vmin=vmin, vmax=vmax, extent=limits)

        # Добавляем цветовую шкалу
        fig.colorbar(im, ax=ax)
        ax.set_ylabel('Latitude')
        ax.set_xlabel('Longitude')
        plt.show()
        

    def paint(self, cmap='binary'):
        fig, ax = plt.subplots(figsize=(12, 7))
        im = ax.imshow(self.data, cmap=cmap)
        fig.colorbar(im, ax=ax)
        plt.show()

    def paint_circulus(self, num_contours=10, color='red'):
        fig, ax = plt.subplots()

        x = np.arange(self.data.shape[1])
        y = np.arange(self.data.shape[0])
        X, Y = np.meshgrid(x, y)

        max_value = np.amax(self.data) * 0.8
        contours = np.linspace(0, max_value, num_contours)

        CS = ax.contour(X, Y, self.data, contours, colors=color)

        im = ax.imshow(self.data, cmap='binary')
        fig.colorbar(im, ax=ax)
        plt.show()
