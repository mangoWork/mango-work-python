# -*- coding: utf-8 -*-
import numpy as np


def multi_arr():
    """
    创建3 x 3的数组
    :return:
    """
    arr = np.array(
        [np.array([np.arange(3), np.arange(3), np.arange(3)]), np.array([np.arange(3), np.arange(3), np.arange(3)]),
         np.array([np.arange(3), np.arange(3), np.arange(3)])])
    # arr = np.array([np.arange(3), np.arange(3), np.arange(3)])
    print arr
    b = np.arange(24).reshape(2, 3, 4)
    print b


def num_type():
    print np.int8(42)
    print np.bool(42)
    return 0


if __name__ == '__main__':
    multi_arr()
    num_type()
