import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as LSC
from pyproj import Geod

def cmap5():
    negative_colors = [(0.0, 'navy'), (0.5, 'skyblue'), (1.0, 'white')]
    negative_cmap = LSC.from_list('negative', negative_colors)

    positive_colors = [(0.0, 'limegreen'), (1.0, 'darkgreen')]
    positive_cmap = LSC.from_list('positive', positive_colors)

    colors = np.vstack((negative_cmap(np.linspace(0, 1, 256)), positive_cmap(np.linspace(0, 1, 256))))
    my_cmap = LSC.from_list('my_cmap', colors)
    return my_cmap
cmap5 = cmap5()

   
def give_description(link):
	#строит карту без ничего
    f = open(link, 'r')
    # Пропуск первой строки (DSAA)
    f.readline()

    # Чтение размеров матрицы
    cols, rows = map(int, f.readline().split())

    # Чтение границ долготы
    lon_min, lon_max = map(float, f.readline().split())

    # Чтение границ широты
    lat_min, lat_max = map(float, f.readline().split())

    # Чтение минимума и максимума чисел в матрице
    min_dep, max_dep = map(float, f.readline().split())

    # Чтение матрицы
    DATA = []
    lines = f.readlines()
    for line in lines:
        for i in line.split():
            DATA.append(float(i))
    DATA = np.array(DATA).reshape(rows, cols)
    DATA = np.flip(DATA, axis=0) #дело в том что в файле строки снизу вверх идут и поэтому так пишем
    f.close()
    return [DATA, [lat_min, lat_max, lon_min, lon_max], [rows, cols]]
   

give_data = lambda link: give_description(link)[0]
	
	
def paint_map(link):
	DATA = give_data(link)
	limits = [give_description(link)[1][i] for i in [2, 3, 0, 1]] #сначала прописывает долготу на осях, потом широту
	max_dep = DATA.max()	
	fig, ax = plt.subplots(figsize=(12, 7)) 
	im = ax.imshow(DATA, cmap=cmap5, vmin=-max_dep, vmax=max_dep, extent = limits) #extent создает границы, а минимум и максимум для нормального отображения цветов

	# Добавляем цветовую шкалу
	fig.colorbar(im, ax=ax)
	ax.set_ylabel('Latitude')
	ax.set_xlabel('Longitude')
	plt.show()
	

def distance(lat1, lon1, lat2, lon2):
    geod = Geod(ellps='WGS84')
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)

    azimuth1, azimuth2, distance = geod.inv(*point1, *point2)
    return distance / 1000
   
   
def coord_data_like(link):
	DATA, limits, size = give_description(link)
	lat_lims = np.linspace(limits[0], limits[1], size[0])
	lon_lims = np.linspace(limits[2], limits[3], size[1])
	DATA_NEW = [(i, q) for i in lat_lims for q in lon_lims]
	DATA_NEW = np.array(DATA_NEW).reshape(size[0], size[1], 2)
	return DATA_NEW
	
 
def distance_data(DATA, *point):
    lat, lon = point
    a, b, c = np.shape(DATA)
    New_data = np.full((a, b), np.nan) #массив той же размерности 
    for i in range(a):
        for q in range(b):
            New_data[i, q] = distance(DATA[i, q, 0], DATA[i, q, 1], lat, lon)
    return New_data
