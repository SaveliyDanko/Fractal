import numpy as np
import matplotlib.pyplot as plt


# Функция для итерации динамической системы Лобача
def lobachevsky_fractal(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        # Преобразование Лобача (примерное формирование функции)
        z = np.sin(z) + c
    return max_iter


# Функция для построения изображения фрактала Лобача
def generate_lobachevsky_fractal(re_min, re_max, im_min, im_max, width, height, max_iter):
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    fractal = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            z = complex(real[j], imag[i])
            c = 0.7885 * np.exp(1j * np.pi / 4)  # Можно варьировать это значение для разных фракталов
            fractal[i, j] = lobachevsky_fractal(c, z, max_iter)

    return fractal


# Параметры изображения
width, height = 800, 800
max_iter = 200  # Максимальное количество итераций

# Диапазоны по вещественной и мнимой осям
re_min, re_max = -2.0, 2.0
im_min, im_max = -2.0, 2.0

# Построение фрактала Лобача
lobachevsky_fractal_image = generate_lobachevsky_fractal(re_min, re_max, im_min, im_max, width, height, max_iter)

# Визуализация фрактала Лобача
plt.figure(figsize=(8, 8))
plt.imshow(lobachevsky_fractal_image.T, cmap='inferno', extent=[re_min, re_max, im_min, im_max])
plt.colorbar()
plt.title("Lobachevsky Fractal")
plt.savefig("lobachevsky_fractal.png")
plt.show()
