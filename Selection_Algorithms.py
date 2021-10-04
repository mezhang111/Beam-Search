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


def split(arr, M):
	A1, A2 = [], []
	for val in arr:
		(A1 if val < M else A2).append(val)
	return A1, A2

def DeterministicSelection(arr,k): 
	n = len(arr)
	subarr_size = 31
	assert k>0 and k<=n, k
	if n <= 2*subarr_size+1:
		return sorted(arr)[n-k]
	else: 
		sets = [arr[x:x+subarr_size] for x in range(0, len(arr),subarr_size)] #partition arr into subsets of subarr_size elements
		medians = [sorted(subset)[(len(subset)-1)//2] for subset in sets] #find medians of all subarrays

		M = DeterministicSelection(medians, (len(medians)+1)//2) #find median of medians
		A1, A2 = split(arr, M); #split arr into 2 subarrays: A1<M, A2 >= M
		if k <= len(A2):
			return DeterministicSelection(A2, k)
		else:
			return DeterministicSelection(A1, k-(n-len(A1)))


def RandomSelection(arr, k):
	n = len(arr)
	assert k>0 and k<=n, k
	if n <= 32:
		return sorted(arr)[n-k]
	else:
		index = random.randint(0,n-1) #pick a random index
		val = arr[index]
		A1, A2 = split(arr, val) #split arr into 2 subarrays: A1 < val, A2 >= val
		if k <= len(A2):
			return RandomSelection(A2, k)
		else:
			return RandomSelection(A1, k-(n-len(A1)))




