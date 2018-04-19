# -*- coding: utf-8 -*-
import numpy as np


def python_sum(n):
    """
    :param n:
    :return:
    """
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


def numpy_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


if __name__ == '__main__':
    python_result = python_sum(3)
    numpy_result = numpy_sum(3)
    print python_result, type(python_result)
    print numpy_result, type(numpy_result)
