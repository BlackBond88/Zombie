from math import pi, atan2, sqrt


def count_angle(x_2, y_2, x_1, y_1):
    """
    Функция, которя считает угол между объектами
    """
    x = x_2 - x_1
    y = y_2 - y_1
    angle = (180 / pi) * atan2(x, y) - 90
    return angle


def count_distance(x_2, y_2, x_1, y_1):
    """
    Функция, которая считает расстояние между двумя точками
    """
    dist = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return dist
