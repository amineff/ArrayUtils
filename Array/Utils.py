import random
import copy


def fill(size, start = 1, end = 10):
	return [random.randint(start, end) for _ in range(size)]

def sort_ascending_classic(arr):
	return sorted(arr, reverse=False)

def isSorted(arr, key = lambda arr: arr):
	return all([key(arr[i]) <= key(arr[i + 1]) for i in range(len(arr) - 1)])

def min(arr):
	value = arr[0]
	for item in arr:
		if item < value:
			value = item
	return value

def sort(arr):
	arr = copy.copy(arr)
	size = len(arr)
	for i1 in range(size):
		for i2 in range(0, size - i1 - 1):
			if arr[i2] > arr[i2 + 1]:
				arr[i2], arr[i2 + 1] = arr[i2 + 1], arr[i2]
	return arr


