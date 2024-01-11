import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):

    # Test empty list
    def test_empty_list(self):
        lavg = ListAverage([])
        assert lavg.compute_avg() == 0.0
        assert lavg.compute_avg_faster() == 0.0

    # Test single element list
    def test_single_element(self):
        lavg = ListAverage([5])
        assert lavg.compute_avg() == 5.0
        assert lavg.compute_avg_faster() == 5.0

    # Test negative numbers
    def test_negative_numbers(self):
        lavg = ListAverage([-2, -4, 6])
        assert lavg.compute_avg() == 0.0
        assert lavg.compute_avg_faster() == 0.0

    # Test decimal numbers
    def test_decimal_numbers(self):
        lavg = ListAverage([1.5, 2.3, 3.7])
        assert lavg.compute_avg() == 2.5
        assert lavg.compute_avg_faster() == 2.5

    # Test large numbers
    def test_large_numbers(self):
        lavg = ListAverage([100000, 200000, 300000])
        assert lavg.compute_avg() == 200000.0
        assert lavg.compute_avg_faster() == 200000.0

    # Test adding numbers
    def test_adding_numbers(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0
        assert lavg.compute_avg_faster() == 2.0
        lavg.add(4)
        assert lavg.compute_avg() == 2.5
        assert lavg.compute_avg_faster() == 2.5

