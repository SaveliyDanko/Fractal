import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета принадлежности к множеству Мандельброта
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Функция для построения изображения множества Мандельброта
def mandelbrot_image(re_min, re_max, im_min, im_max, width, height, max_iter):
    # Создание сетки для комплексных чисел
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    mandelbrot_set = np.zeros((height, width))

    # Вычисление множества Мандельброта для каждой точки сетки
    for i in range(height):
        for j in range(width):
            c = complex(real[j], imag[i])
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)

    return mandelbrot_set

# Параметры изображения
width, height = 800, 800
max_iter = 200  

# Диапазоны по вещественной и мнимой осям
re_min, re_max = -2.0, 1.0
im_min, im_max = -1.5, 1.5

# Построение множества Мандельброта
mandelbrot_set = mandelbrot_image(re_min, re_max, im_min, im_max, width, height, max_iter)

# Визуализация множества Мандельброта
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set.T, cmap='inferno', extent=[re_min, re_max, im_min, im_max])
plt.colorbar()
plt.title("Mandelbrot Set Visualization")

# Сохранение изображения в файл
plt.savefig("mandelbrot_set.png")
