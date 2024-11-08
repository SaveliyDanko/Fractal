import numpy as np
import matplotlib.pyplot as plt


# Функция для применения метода Ньютона
def newton_method(z, max_iter):
    for i in range(max_iter):
        try:
            z_next = z - (z ** 3 - 1) / (3 * z ** 2)
        except ZeroDivisionError:
            return i

        if abs(z_next - z) < 1e-6:
            break
        z = z_next
    return z


# Функция для создания фрактала Ньютона
def newton_fractal(re_min, re_max, im_min, im_max, width, height, max_iter):
    real = np.linspace(re_min, re_max, width)
    imag = np.linspace(im_min, im_max, height)
    fractal = np.zeros((height, width, 3))

    # Три корня уравнения z^3 - 1 = 0
    roots = [1, np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3)]

    for i in range(height):
        for j in range(width):
            z = complex(real[j], imag[i])
            z_final = newton_method(z, max_iter)

            # Определяем цвет на основе того, к какому корню сходится
            if abs(z_final - roots[0]) < 1e-6:
                fractal[i, j] = [1, 0, 0]  # Красный для корня 1
            elif abs(z_final - roots[1]) < 1e-6:
                fractal[i, j] = [0, 1, 0]  # Зелёный для корня e^(2πi/3)
            elif abs(z_final - roots[2]) < 1e-6:
                fractal[i, j] = [0, 0, 1]  # Синий для корня e^(4πi/3)
            else:
                fractal[i, j] = [0, 0, 0]  # Чёрный для точек, которые не сходятся

    return fractal


# Параметры изображения
width, height = 800, 800
max_iter = 50  # Количество итераций

# Диапазоны по вещественной и мнимой осям
re_min, re_max = -1.5, 1.5
im_min, im_max = -1.5, 1.5

# Построение фрактала Ньютона
newton_fractal_image = newton_fractal(re_min, re_max, im_min, im_max, width, height, max_iter)

# Визуализация фрактала Ньютона
plt.figure(figsize=(10, 10))
plt.imshow(newton_fractal_image, extent=[re_min, re_max, im_min, im_max])
plt.title("Newton's Fractal for $z^3 - 1 = 0$")
plt.savefig("newton_fractal.png")
plt.show()
