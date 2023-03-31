
import numpy as np


def dot(u, v):
    return np.sum([ux*vx for ux, vx in zip(u, v)])


def gauss1(v1, v2):
    while True:
        if dot(v1, v1) > dot(v2, v2):
            v1, v2 = v2, v1
        m = dot(v1, v2) // dot(v1, v1)
        if m == 0:
            return v1, v2   
        v2 = [v2x-m*v1x for v1x, v2x in zip(v1, v2)]


u = [87502093, 123094980]
v = [846835985, 9834798552]

u, v = gauss1(u, v)
print(dot(u, v))

