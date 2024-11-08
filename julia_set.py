import numpy as np
import matplotlib.pyplot as plt


# Функция для расчета принадлежности к множеству Жюлиа
def julia(z, c, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# Функция для построения изображения множества Жюлиа
def julia_set_image(c, re_min, re_max, im_min, im_max, width, height, max_iter):
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    julia_set = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            z = complex(real[j], imag[i])
            julia_set[i, j] = julia(z, c, max_iter)

    return julia_set


# Параметры изображения
width, height = 800, 800
max_iter = 300  # Количество итераций

# Диапазоны по вещественной и мнимой осям
re_min, re_max = -1.5, 1.5
im_min, im_max = -1.5, 1.5

# Комплексное число c для множества Жюлиа (можно менять для других изображений)
c = complex(-0.5251993, 0.5251993)

# Построение множества Жюлиа
julia_set = julia_set_image(c, re_min, re_max, im_min, im_max, width, height, max_iter)

# Визуализация множества Жюлиа
plt.figure(figsize=(10, 10))
plt.imshow(julia_set.T, cmap='inferno', extent=[re_min, re_max, im_min, im_max])
plt.colorbar()
plt.title(f"Julia Set for c = {c}")
plt.savefig("julia_set.png")
