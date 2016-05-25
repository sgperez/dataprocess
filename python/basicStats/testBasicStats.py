import unittest
from basicStats import BasicStats
from math import sqrt

class TestBasicStats(unittest.TestCase):
	def test_create_list(self):
		stat_obj = BasicStats()
		self.assertEqual(len(stat_obj.creates_random_array(5)), 5)

	def test_mean(self):
		stat_obj = BasicStats()
		self.assertEqual(stat_obj.get_mean([1,2,3]), 2)

	def test_variance(self):
		stat_obj = BasicStats()
		self.assertEqual(stat_obj.get_variance([1,2,3]), 2/3)

	def test_standard_deviation(self):
		stat_obj = BasicStats()
		self.assertEqual(stat_obj.get_standard_deviation([1,2,3]), sqrt(float(2/3)))		


if __name__ == '__main__':
    unittest.main()
