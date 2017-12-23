import unittest
import sys
sys.path.insert(0,'../')

from pppr import aabb

class Testaabbmetry(unittest.TestCase):

    def test_inside_aabb(self):
        bb = (0, 0, 10, 10)
        self.assertTrue(aabb.is_inside(bb,(5,5)))
        self.assertTrue(aabb.is_inside(bb,(9,9)))
        self.assertTrue(aabb.is_inside(bb,(0,0)))
        self.assertTrue(aabb.is_inside(bb,(0,9)))

        self.assertFalse(aabb.is_inside(bb,(0,-9)))
        self.assertFalse(aabb.is_inside(bb,(-1,-1)))


    def test_inside_negative_aabb(self):
        bb = (-20, -20, 10, 10)
        self.assertFalse(aabb.is_inside(bb,(5,5)))
        self.assertFalse(aabb.is_inside(bb,(9,9)))
        self.assertFalse(aabb.is_inside(bb,(0,0)))
        self.assertFalse(aabb.is_inside(bb,(0,9)))
        self.assertFalse(aabb.is_inside(bb,(0,-9)))
        self.assertFalse(aabb.is_inside(bb,(-1,-1)))

        self.assertTrue(aabb.is_inside(bb,(-15,-15)))
        self.assertTrue(aabb.is_inside(bb,(-19,-19)))
        self.assertTrue(aabb.is_inside(bb,(-11,-15)))
        self.assertTrue(aabb.is_inside(bb,(-20,-19)))

    def test_intersection(self):
        A = (0, 0, 10, 10)
        B = (5, 0, 10, 10)
        int_ab = aabb.intersection(A, B)
        self.assertEqual(int_ab, 5*10)

        A = (0, 0, 10, 10)
        B = (15, 0, 10, 10)
        int_ab = aabb.intersection(A, B)
        self.assertEqual(int_ab, 0)

        int_ab = aabb.intersection(A, A)
        self.assertEqual(int_ab, 10*10)

        A = (5, 0, 5, 15)
        B = (0, 5, 15, 5)
        I = aabb.intersection(A, B)
        self.assertEqual(I, 5*5)

    def test_union(self):
        A = (0, 0, 10, 10)
        B = (5, 0, 10, 10)
        int_ab = aabb.union(A, B)
        self.assertEqual(int_ab, 2*10*10 - 5*10)

        A = (0, 0, 10, 10)
        B = (15, 0, 10, 10)
        int_ab = aabb.union(A, B)
        self.assertEqual(int_ab, 2*10*10)

        int_ab = aabb.union(A, A)
        self.assertEqual(int_ab, 10*10)

    def test_fail_iou(self):
        """ things that failed while using the library
        """
        A = (1359, 413, 120, 362)
        B = (1255, 447, 33, 100)
        self.assertEqual(aabb.intersection(A, B), 0)

        A = (10, 10, 10, 10)
        B = (5, 5, 2, 2)
        I = aabb.intersection(A, B)
        U = aabb.union(A, B)
        self.assertEqual(aabb.intersection(A, B), 0)

        self.assertTrue(aabb.IoU(A, B) < 1)

        A = (7, 5, 6, 5)
        B = (5, 6, 10, 5)
        I = aabb.intersection(A, B)
        self.assertTrue(I > 0)


        A = (1359, 413, 120, 362)
        B = (1338.0, 418.0, 167.0, 379.0)

        I = aabb.intersection(A, B)

        self.assertTrue(aabb.IoU(A, B) > 0)

    def test_iou(self):
        A = (0, 0, 10, 10)
        B = (5, 0, 10, 10)
        self.assertEqual(aabb.IoU(A, B), 1/3, 0.000001)

        A = (0, 0, 10, 10)
        B = (15, 0, 10, 10)
        self.assertEqual(aabb.IoU(A, B), 0, 0.000001)

        A = (0, 0, 10, 10)
        B = (3.33333333, 0, 10, 10)
        self.assertTrue(aabb.IoU(A, B) > 0.49 and \
            aabb.IoU(A, B) < 0.51)

if __name__ == '__main__':
    unittest.main()
