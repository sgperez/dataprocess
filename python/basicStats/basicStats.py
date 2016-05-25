from random import random
from math import sqrt

class BasicStats:


	#def __init__(lista):


	def creates_random_array(self, items_no=10):
		new_list = []
		try:
			int(items_no)
			if items_no < 0:
				items_no = 10
		except ValueError:
			items_no = 10


		for num in range(0,items_no):
			new_list.append(int(random() * 100))
		return new_list


	def get_mean(self, exp_list):
		total_el = len(exp_list)

		if total_el > 0:
			total_val = 0
			for el in exp_list:
				total_val += el
			return float(total_val) / float(total_el)
		else:
			return 0


	def get_median(self, exp_list):
		total_el = len(exp_list)

		#sort lit
		exp_list.sort()

		if total_el > 0:
			if total_el % 2 == 0:
				right_val = total_el / 2
				left_val = right_val - 1
				return float(exp_list[left_val] + exp_list[right_val]) / float(2)
			else:
				return exp_list[total_el / 2]
		else:
			return 0

	def get_variance(self, exp_list):
		total_el = len(exp_list)
		mean = self.get_mean(exp_list)

		if total_el > 0:
			total_val = 0
			for el in exp_list:
				total_val += pow((el - mean),2)
			return float(total_val) / float(total_el)
		else:
			return 0


	def get_standard_deviation(self, exp_list):
		return sqrt(self.get_variance(exp_list))
