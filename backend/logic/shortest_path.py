from python_tsp.exact import solve_tsp_dynamic_programming
import numpy as np
import math


def travelling_salesmen_problem(points, startIdx=0, circular=True):
    get_x = lambda point: point["location"]["lat"]
    get_y = lambda point: point["location"]["lng"]

    size = len(points)

    _swap(points, 0, startIdx)
    distance_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(0 if circular else 1, size):
            distance_matrix[i][j] = _find_distance(points[i], points[j], get_x, get_y)

    permutation, distance = solve_tsp_dynamic_programming(np.array(distance_matrix))

    return list(map(lambda p: points[p], permutation))


def _find_distance(point_a, point_b, get_x, get_y):
    point_a = [get_x(point_a), get_y(point_a)]
    point_b = [get_x(point_b), get_y(point_b)]
    return math.dist(point_a, point_b)


def _swap(points, a, b):
    points[a], points[b] = points[b], points[a]
    return points
