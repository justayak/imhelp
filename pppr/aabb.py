import numpy as np
from math import sqrt

def dist(bb1, bb2):
    x1, y1, w1, h1 = bb1
    x2, y2, w2, h2 = bb2

    X1, Y1 = x1 + w1/2, y1 + h1/2
    X2, Y2 = x2 + w2/2, y2 + h2/2
    return sqrt((X1 - X2)**2 + (Y1 - Y2)**2)

def is_inside(aabb, point):
    """ tests if a point is inside an aabb

    aabb: (x,y,w,h)
    point: (x,y)

    """
    x,y,w,h = aabb
    u,v = point
    return u >= x and u < x+w and \
        v >= y and v < y+h


def intersection(bb1, bb2):
    """ Calculates the Intersection of two aabb's
    """
    min_w = min(bb1[2], bb2[2])
    min_h = min(bb1[3], bb2[3])
    if bb1[0] < bb2[0]:
        leftbb, rightbb = bb1, bb2
    else:
        leftbb, rightbb = bb2, bb1

    if bb1[1] < bb2[1]:
        topbb, bottombb = bb1, bb2
    else:
        topbb, bottombb = bb2, bb1

    w = min(min_w, max(leftbb[0] + leftbb[2] - rightbb[0], 0))
    h = min(min_h, max(topbb[1] + topbb[3] - bottombb[1], 0))
    return w * h


def union(bb1, bb2):
    """ Calculates the Union of two aabb's
    """
    _, _, w1, h1 = bb1
    _, _, w2, h2 = bb2
    return w1 * h1 + w2 * h2 - intersection(bb1, bb2)


def IoU(bb1, bb2):
    """ Calculate the Intersection over Union
        of two AABB's

    aabb: (x,y,w,h)

    x---m---x
    |       |
    |       h
    |       |
    x-------x

    """
    I = intersection(bb1, bb2)
    U = union(bb1, bb2)
    return I/U
