import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def cmap5():
    negative_colors = [(0.0, 'navy'), (0.5, 'skyblue'), (1.0, 'white')]
    negative_cmap = LSC.from_list('negative', negative_colors)

    positive_colors = [(0.0, 'limegreen'), (1.0, 'darkgreen')]
    positive_cmap = LSC.from_list('positive', positive_colors)

    colors = np.vstack((negative_cmap(np.linspace(0, 1, 256)), positive_cmap(np.linspace(0, 1, 256))))
    my_cmap = LSC.from_list('my_cmap', colors)
    return my_cmap

   
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
    return [DATA, [lon_min, lon_max, lat_min, lat_max]]
   

give_data = lambda link: give_description(link)[0]
	
	
def paint_map(link):
	DATA = give_data(link)
	# Создаем фигуру и ось
	fig, ax = plt.subplots(figsize=(12, 7))  # Изменяем размер фигуры

	# Рисуем карту с помощью imshow()
	im = ax.imshow(DATA, cmap=cmap5, vmin=-max_dep, vmax=max_dep)

	# Добавляем цветовую шкалу
	fig.colorbar(im, ax=ax)
	
    