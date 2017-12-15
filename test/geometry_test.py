import unittest
import sys
sys.path.insert(0,'../')

from pppr import geometry

class TestGeometry(unittest.TestCase):

    def test_inside_aabb(self):
        aabb = (0, 0, 10, 10)
        self.assertTrue(geometry.is_inside_aabb(aabb,(5,5)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(9,9)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(0,0)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(0,9)))

        self.assertFalse(geometry.is_inside_aabb(aabb,(0,-9)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(-1,-1)))


    def test_inside_negative_aabb(self):
        aabb = (-20, -20, 10, 10)
        self.assertFalse(geometry.is_inside_aabb(aabb,(5,5)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(9,9)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(0,0)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(0,9)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(0,-9)))
        self.assertFalse(geometry.is_inside_aabb(aabb,(-1,-1)))

        self.assertTrue(geometry.is_inside_aabb(aabb,(-15,-15)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(-19,-19)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(-11,-15)))
        self.assertTrue(geometry.is_inside_aabb(aabb,(-20,-19)))


if __name__ == '__main__':
    unittest.main()
