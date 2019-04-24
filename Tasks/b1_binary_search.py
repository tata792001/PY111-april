def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
		"""
	left_b = -1
	right_b = len(arr)-1
	while right_b > left_b+1:
		middle = (left_b + right_b)//2
		if arr[middle] > elem:
			right_b = middle
		else:
			left_b = middle
			
	if elem == arr[right_b]:
		return right_b
	elif elem == arr[left_b]:
		return left_b
	else:
		return None