import heapq
import numpy as np

def BubbleSelection(arr,k): #returns the value of the k-th biggest element, note that this algo changes the ordering of the array
	n = len(arr)
	assert k>0 and k<=n, k
	for i in range(k):
		for j in range(n-2, -1, -1):
			if arr[j] < arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	
	return arr[k-1]

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

def partition_into_5er_set(arr): #for derteministic select
	n = len(arr)
	k = (n+4)//5 #number of subarrays
	#for efficiency we use numpy instead of list, the last subarry could have redundant entries. 
	sets = np.empty(shape = (k,5)) 
	for i in range(k):
		for j in range(5):
			if(i*5+j > n-1): 
				break
			sets[i][j] = arr[i*5+j]

	return sets


def split(arr, M): #for derteministic select
	n = len(arr)
	l1 = l2 = l3 = 0
	#find length for each array
	for i in range(n):
		if arr[i] < M:
			l1 = l1+1
		elif arr[i] > M:
			l3 = l3+1
		else:
			l2 = l2+1
	A1 = np.empty(l1)
	A2 = np.empty(l2)
	A3 = np.empty(l3)
	
	for i in range(n):
		if arr[i] < M:
			l1 = l1-1
			A1[l1] = arr[i]
		elif arr[i] > M:
			l3 = l3-1
			A3[l3] = arr[i]
		else:
			l2 = l2-1
			A2[l2] = arr[i]
	return A1, A2, A3

def DeterministicSelection(arr,k): 
	n = len(arr)
	assert k>0 and k<=n, k
	if n <= 10:
		return (HeapSelection(arr, k))
	else: 
		sets = partition_into_5er_set(arr) #partition arr into subsets of 5 elements
		num_subsets = (n+4)//5
		medians = np.empty(num_subsets)
		for i in range(num_subsets - 1):
			medians[i] = DeterministicSelection(sets[i], 3) #find median of subarray in O(1)
		#handle edge case
		rest = n%5
		assert rest >= 0
		if rest == 0:
			medians[num_subsets-1] = DeterministicSelection(sets[num_subsets-1], 3)
		else:
			medians[num_subsets-1] = DeterministicSelection(sets[num_subsets-1][0:rest+1], (rest+1)//2)

		M = DeterministicSelection(medians, (num_subsets+1)//2) #find median of medians
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
	if n <= 10:
		return (HeapSelection(arr, k))
	else:
		index = np.random.randint(low = 0, high = n, size = 1) #pick a random index
		A1, A2, A3 = split(arr, arr[index]) #split arr into 3 subarrays: A1 < arr[index], A2 = arr[index], A3 > arr[index]
		if k <= len(A3):
			return RandomSelection(A3, k)
		elif k > len(A3) + len(A2):
			return RandomSelection(A1, k-len(A3)-len(A2))
		else:
			return arr[index]

def testcases(f1, f2, f3, f4):
	for i in range(10):
		for k in range(1,101):
			arr = np.random.rand(100) - np.random.rand(100)
			assert f1(arr,k) == f2(arr,k) == f3(arr,k) == f4(arr, k)
	print("succeed")


def main():
	testcases(BubbleSelection, HeapSelection, DeterministicSelection, RandomSelection)


if __name__ == "__main__":
	main()
