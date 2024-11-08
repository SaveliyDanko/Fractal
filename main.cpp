#include <SFML/Graphics.hpp>
#include <iostream>
#include <cmath>
#include <vector>

const int WIDTH = 10000, HEIGHT = 10000;
const int MAX_ITERATIONS = 1000;
const std::pair<double, double> c = std::make_pair(-0.5251993, 0.5251993);
const int R = 4;


std::pair<double, double> square_zulia(std::pair<double, double> z_1, std::pair<double, double> z_2) {
    double x = z_1.first * z_2.first - z_1.second * z_2.second;
    double y = z_1.first * z_2.second + z_1.second * z_2.first;
    return std::make_pair(x, y);
}

std::pair<double, double> f(std::pair<double, double> z, int n) {
    std::pair<double, double> r = z;
    for (int i = 0; i < n - 1; i++) {
        r = square_zulia(r, z);
    }
    double x = r.first + c.first;
    double y = r.second + c.second;
    return std::make_pair(x, y);
}

int zulia()
{
    sf::Image image;
    image.create(WIDTH, HEIGHT);

    std::vector<std::vector<int>> coords(HEIGHT, std::vector<int>(WIDTH, -1));
    for (int i = 0; i < image.getSize().y; i++) {
        for (int j = 0; j < image.getSize().x; j++) {
            std::pair<double, double> z = std::make_pair(3 * ((double) i - HEIGHT / 2) / HEIGHT, 3 * ((double) j - WIDTH / 2) / WIDTH);
            for (int k = 0; k < MAX_ITERATIONS; k++) {
                z = f(z, 2);
                if (z.first * z.first + z.second * z.second > R) {
                    coords[i][j] = k;
                    break;
                }
            }
        }
    }

    for (unsigned int x = 0; x < image.getSize().x; ++x) {
        for (unsigned int y = 0; y < image.getSize().y; ++y) {
            image.setPixel(x, y, sf::Color::White);
        }
    }

    for (int y = 0; y < image.getSize().y; y++) {
        for (int x = 0; x < image.getSize().x; x++) {
            int k = coords[y][x];
            image.setPixel(y, x, sf::Color((int)(255 * std::sin(k)), (int)(255 * std::sin(k)), (int)(255 * std::sin(k))));
        }
    }

    if (!image.saveToFile("output.png")) {
        std::cerr << "Ошибка при сохранении файла." << std::endl;
        return 1;
    }

    std::cout << "Изображение успешно сохранено как output.png" << std::endl;

    return 0;
}



int mal()
{
    sf::Image image;
    image.create(WIDTH, HEIGHT);

    std::vector<std::vector<int>> coords(HEIGHT, std::vector<int>(WIDTH, 0));
    double koeff = 2 * std::sqrt(2.0 / (double)(HEIGHT * HEIGHT + WIDTH * WIDTH));
    for (int i = 0; i < image.getSize().y; i++) {
        for (int j = 0; j < image.getSize().x; j++) {
            std::pair<double, double> z = std::make_pair(0, 0);
            std::pair<double, double> c = std::make_pair(koeff * (i - 3 * HEIGHT / 4), koeff * (j - WIDTH / 2));
            for (int k = 0; k < MAX_ITERATIONS; k++) {
                double x_tmp = z.first * z.first - z.second * z.second + c.first;
                double y_tmp = 2 * z.first * z.second + c.second;
                z.first = x_tmp;
                z.second = y_tmp;

                if (std::sqrt(x_tmp * x_tmp + y_tmp * y_tmp) > 2) {
                    coords[i][j] = k;
                    break;
                }
            }
        }
    }

    for (unsigned int x = 0; x < image.getSize().x; ++x) {
        for (unsigned int y = 0; y < image.getSize().y; ++y) {
            image.setPixel(x, y, sf::Color::White);
        }
    }

    for (int y = 0; y < image.getSize().y; y++) {
        for (int x = 0; x < image.getSize().x; x++) {
            int k = coords[y][x];
            image.setPixel(y, x, sf::Color((int)(255 * std::sin(k)), (int)(255 * std::sin(k)), (int)(255 * std::sin(k))));
        }
    }

    if (!image.saveToFile("output.png")) {
        std::cerr << "Ошибка при сохранении файла." << std::endl;
        return 1;
    }

    std::cout << "Изображение успешно сохранено как output.png" << std::endl;

    return 0;
}


int main() {
    zulia();
    return 0;
}