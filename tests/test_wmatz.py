#!/usr/bin/env python
import unittest
from wmatz import WeightedPointZ, WeightedMeanCenterZ, WeightedMatCenterZ


class WmatzTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_points = {'A': WeightedPointZ(3.0, 0.0, 0.0, 1.0),
                              'B': WeightedPointZ(14.0, 3.0, 0.0, 1.0),
                              'C': WeightedPointZ(10.0, 4.0, 0.0, 1.0),
                              'D': WeightedPointZ(13.0, 11.0, 0.0, 1.0),
                              'E': WeightedPointZ(4.0, 13.0, 0.0, 1.0),
                              'F': WeightedPointZ(0.0, 8.0, 0.0, 1.0)}

    def test_mean(self):
        mean = WeightedMeanCenterZ()
        for pt in self.sample_points:
            mean.step(self.sample_points[pt])
        actual = mean.finalize()
        expected = WeightedPointZ(7.33, 6.5, 0.0)
        self.assertAlmostEqual(actual.x, expected.x, places=2)
        self.assertAlmostEqual(actual.y, expected.y, places=2)
        self.assertAlmostEqual(actual.z, expected.z, places=2)

    def test_mat(self):
        mat = WeightedMatCenterZ()
        for pt in self.sample_points:
            mat.step(self.sample_points[pt])
        actual = mat.finalize()
        expected = WeightedPointZ(8.58, 5.61, 0.0)
        self.assertAlmostEqual(actual.x, expected.x, places=2)
        self.assertAlmostEqual(actual.y, expected.y, places=2)
        self.assertAlmostEqual(actual.z, expected.z, places=2)


if __name__ == '__main__':
    unittest.main()
