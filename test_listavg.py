import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    # add more unit tests below
