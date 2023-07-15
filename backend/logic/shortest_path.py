from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_simulated_annealing
import numpy as np
import math


def travelling_salesmen_problem(points, startIdx=0, circular=True):
    get_x = lambda point: point["details"]["location"]["lat"]
    get_y = lambda point: point["details"]["location"]["lng"]

    size = len(points)

    # TODO might not work in case of smaller sets
    _swap(points, 0, startIdx)
    distance_matrix = [[0] * size] * size

    for i in range(size):
        if i == 0 and not circular:
            continue
        for j in range(size):
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
