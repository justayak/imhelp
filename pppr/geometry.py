import numpy as np

def is_inside_aabb(aabb, point):
    """ tests if a point is inside an aabb

    aabb: (x,y,w,h)
    point: (x,y)

    """
    x,y,w,h = aabb
    u,v = point
    return u >= x and u < x+w and \
        v >= y and v < y+h
