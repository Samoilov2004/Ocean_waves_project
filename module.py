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


def cmap_final():
	# Создаем цветовую карту
	colors_list = [[0, 'black'], [0.001, 'white'], [1, 'red']]
	cmap = LSC.from_list('custom_cmap', colors_list)
	return cmap_final

cmap1 = cmap_final()


def get_description(file_path):
    with open(file_path, 'r') as f:
        f.readline()  # Пропуск первой строки (DSAA)

        n_cols, n_rows = map(int, f.readline().split())
        lon_min, lon_max = map(float, f.readline().split())
        lat_min, lat_max = map(float, f.readline().split())
        min_depth, max_depth = map(float, f.readline().split())

        data = [float(value) for value in f.read().split()]
        data = np.array(data).reshape(n_rows, n_cols)
        data = np.flip(data, axis=0)  # дело в том что в файле строки снизу вверх идут и поэтому так пишем

    return data, [lat_min, lat_max, lon_min, lon_max], [n_rows, n_cols]


get_data = lambda file_path: get_description(file_path)[0]


def paint_map(link):
	DATA = get_data(link)
	limits = [get_description(link)[1][i] for i in [2, 3, 0, 1]] #сначала прописывает долготу на осях, потом широту
	max_dep = DATA.max()	
	fig, ax = plt.subplots(figsize=(12, 7)) 
	im = ax.imshow(DATA, cmap=cmap5, vmin=-max_dep, vmax=max_dep, extent = limits) #extent создает границы, а минимум и максимум для нормального отображения цветов

	# Добавляем цветовую шкалу
	fig.colorbar(im, ax=ax)
	ax.set_ylabel('Latitude')
	ax.set_xlabel('Longitude')
	plt.show()
	
	
def paint(DATA):
	fig, ax = plt.subplots(figsize=(12, 7)) 
	im = ax.imshow(DATA, cmap='binary') 
	fig.colorbar(im, ax=ax)
	plt.show()
	

def paint_circulus(DATA):
    fig, ax = plt.subplots()

    x = np.arange(DATA.shape[1])
    y = np.arange(DATA.shape[0])
    X, Y = np.meshgrid(x, y)
 
    max_value = np.amax(DATA) * 0.8
    num_contours = np.arange(0, max_value, 5)

    CS = ax.contour(X, Y, DATA, num_contours, colors = 'red')

    im = ax.imshow(DATA, cmap='binary')
    fig.colorbar(im, ax=ax)
    plt.show()
    
    
def paint_scores(DATA):
	DATA /= DATA.max()
	plt.imshow(y, cmap=cmap_final, vmin=0, vmax=1)
	plt.colorbar()
	plt.show()

		
def distance(lat1, lon1, lat2, lon2):
	#работает для ввода долготы в 360
    if lon1 > 180:
        lon1 = lon1-360
    if lon2 > 180:
        lon2 = lon2-360
    geod = Geod(ellps='WGS84')
    point1 = (lon1, lat1)
    point2 = (lon2, lat2)

    azimuth1, azimuth2, distance = geod.inv(*point1, *point2)
    return distance / 1000
   
   
def coord_data_like(link):
	DATA, limits, size = get_description(link)
	lat_lims = np.linspace(limits[1], limits[0], size[0]) #чтобы массив был сверху вниз
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
   
   
def triangle_time(link, lat, lon, lat_volcano=-20.5333, lon_volcano=184.6333):
	v = 1116 #310 м/с
	DATA, limits, size = get_description(link)
	
	COORD_DATA = coord_data_like(link)
	DATA_AIR = distance_data(COORD_DATA, lat_volcano, lon_volcano) / v
	return DATA + DATA_AIR


def accuracy_data(DATA, type=2, time=0):
	if type == 1:
		return np.abs(data - time)
	else:
		abs_data = np.abs(data - time)
		return (abs_data) ** type
       

		
	
