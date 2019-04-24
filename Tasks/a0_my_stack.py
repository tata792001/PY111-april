"""
My little Stack
"""
stack = [1,2,3,4,5]

def push(elem) -> None:

	stack.append(None)


	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""

	return stack




def pop():
	stack.pop()



	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	return stack


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	return None
