import heapq
import numpy as np
import random

def BubbleSelection(arr,k): #returns the value of the k-th biggest element
	n = len(arr)
	assert k>0 and k<=n, k
	temp = np.empty(n)
	for i in range(n):
		temp[i] = arr[i]

	for i in range(k):
		for j in range(n-2, -1, -1):
			if temp[j] < temp[j+1]:
				curr = temp[j]
				temp[j] = temp[j+1]
				temp[j+1] = curr
	
	return temp[k-1]

def HeapSelection(arr,k): 
	n = len(arr)
	assert k>0 and k<=n, k
	candidates = []
	for value in arr:
		if len(candidates) < k:
			heapq.heappush(candidates, value)
		else:
			curr_min = candidates[0] #current min
			if(curr_min < value):
				heapq.heappop(candidates)
				heapq.heappush(candidates, value)

	return candidates[0]

def partition_into_5er_set(arr): 
	n = len(arr)
	sets = []
	index = 0
	while index+5 < n:
	    sets.append(arr[index:index+5])
	    index += 5
	sets.append(arr[index:])

	return sets


def split(arr, M): #for derteministic select
	A1 = []
	A2 = []
	A3 = []
	for val in arr:
		if val < M:
		    A1.append(val)
		elif val > M:
		    A3.append(val)
		else:
		    A2.append(val)

	return A1, A2, A3

def DeterministicSelection(arr,k): 
	n = len(arr)
	assert k>0 and k<=n, k
	if n <= 20:
		#return (HeapSelection(arr, k))
		return sorted(arr)[n-k]
	else: 
		sets = partition_into_5er_set(arr) #partition arr into subsets of 5 elements
		medians = []
		for subset in sets:
			l = len(subset)
			medians.append(DeterministicSelection(subset, (l+1)//2)) #find median of subarray in O(1)

		M = DeterministicSelection(medians, (len(medians)+1)//2) #find median of medians
		A1, A2, A3 = split(arr, M); #split arr into 3 subarrays: A1<M, A2 = M, A3 > M
		if k <= len(A3):
			return DeterministicSelection(A3, k)
		elif k > len(A3) + len(A2):
			return DeterministicSelection(A1, k-len(A3)-len(A2))
		else:
			return M

def RandomSelection(arr, k):
	n = len(arr)
	assert k>0 and k<=n, k
	if n <= 20:
		#return (HeapSelection(arr, k))
		return sorted(arr)[n-k]
	else:
		index = random.randint(0,n-1) #pick a random index
		A1, A2, A3 = split(arr, arr[index]) #split arr into 3 subarrays: A1 < arr[index], A2 = arr[index], A3 > arr[index]
		if k <= len(A3):
			return RandomSelection(A3, k)
		elif k > len(A3) + len(A2):
			return RandomSelection(A1, k-len(A3)-len(A2))
		else:
			return arr[index]



