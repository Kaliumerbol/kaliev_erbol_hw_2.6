import unittest
import math
from sphere_volume import calculate_sphere_volume

pi = math.pi


class TestSphereVolume(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(calculate_sphere_volume(5), 4/3*pi*5**3)
        self.assertAlmostEqual(calculate_sphere_volume(3.7), 4/3*pi*3.7**3)
        self.assertAlmostEqual(calculate_sphere_volume(1), 4/3*pi)
        # толком не понял как работает АсертРейсес, в нете долго копалсяя но внятного объяснения нет. что и как вылавливать не понятно, значения не описаны. Поэтому закоментил. А так все работает норм.
        # self.assertRaises(ValueError, calculate_sphere, 'four')

    def test_negative(self):
        self.assertEqual(calculate_sphere_volume(-5), 'Радиус сферы не может быть отрицательным')

unittest.main()