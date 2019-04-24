"""
This module implements some functions based on linear search algo
"""
import numpy
import random

def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	num = 0
	for i in range(len(arr)):
		if arr[i] < arr[num]:
			num = i
	return arr[num]


def min_weight_search(Graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param Graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""

	return None, None