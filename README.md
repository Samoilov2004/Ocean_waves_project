# Ocean_waves_project

Под DATA везде дальше подразумевается матрица размерности 2 произвольного размера (обычно такого же, что и указано в файле.)

Недописаны/багованые - 5, 9, 10.

## 1. cmap5(None) -> cmap
Функция `cmap5()` создает пользовательскую цветовую палитру для визуализации карты. Палитра состоит из двух градиентов: от темно-синего цвета для минимального значения до белого для нулевого значения и от желто-зеленого цвета для нулевого значения до темно-зеленого для максимального значения. Палитра не является непрерывной функцией, что позволяет четко различать границу жидкости и суши на значении 0 метров.

## 2. get_description(link) -> [DATA, [lat_min, lat_max, lon_min, lon_max], [rows, cols] ]

Возвращает массив с матрицей, границами карты и размером матрицы. В output не добавлена информация о минимумах и максимумах, так как эта информация избыточна.

## 3. get_data(link) -> DATA

Настроено для grd файлов. По сути частный случай прошлой функции.

## 4. paint_map(link) -> plot

Функция `paint_map(link)` рисует карту на основе данных из файла с использованием созданной пользовательской цветовой палитры, стоит карту без изоклинов. 

## 5. paint(DATA) -> plot

Очень простая функция которая по массиву что-то строит, используется просто для ознакомления с данными.

## 6. paint_circulus(DATA) -> plot

По данным о времени строит круговые линии прихода волны в разные точки.

## 7. paint_scores(DATA) -> plot

## 8. distance(lat1, lon1, lat2, lon2) -> km

Функция `distance(lat1, lon1, lat2, lon2)` вычисляет расстояние между двумя точками на поверхности Земли по их координатам (широта и долгота) в километрах. Функция использует библиотеку pyproj и метод inv класса Geod для вычисления расстояния по эллипсоиду WGS84. 

## 9. coord_data_like(link) -> DATA

Функция `coord_data_like(link)` создает матрицу/двумерный массив такого же размера, как и в файле, но в каждом узле стоят его (lat, lon) координаты. Мало используется в интерфейсе, но для удобства наследуется в других функциях.

## 10. distance_data(link, lat, lon) -> DATA

Создает массив того же размера, что и DATA из link, но в каждой точке сидят не координаты и не глубина, а расстояние до точки, которая будет указана в аргументе. 

## 11. triangle_time(link, lat, lon) -> DATA

Функция `triangle_time(link, lat, lon)` создает матрицу времени добегания волны от вулкана Тонга до станции через 3 точку (в каждом узле сетке написано время с тем условием, что третья точка - этот самый узел). Предполагается что до третьей точки волна шла со скоростью атмосферной волны (310 м/с), а после - с скоростью гравитационной волны. link - ссылка на файл, что содержит времена добегания атмосферной волны до каждой точки. 

## 12. accuracy_data(DATA, type=2, time=0) -> DATA

Функция возвращает массив отклонений DATA от заданного значения time. Если type равен 1, функция вычисляет абсолютное отклонение. Если type не равен 1, функция вычисляет абсолютное отклонение в степени type.


