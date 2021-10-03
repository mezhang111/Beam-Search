import Selector as s
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm

def test_with_time_measure(selector, arr, k):
	start = time.time()
	res = selector.select(arr,k)
	end = time.time()
	return (end-start), res

def testcases(selector_list, n, k):
	l = len(selector_list)
	times = np.zeros(shape = l)
	for i in range(10): #average in 10 times
		arr = np.random.normal(0,100,n)
		vals = np.empty(shape = l)
		for i in range(l):
			t, res = test_with_time_measure(selector_list[i],arr,k)
			times[i] = t
			vals[i] = res
		for i in range(l-1):
			assert vals[i] == vals[i+1] #check if the results agree with each other

	times = times/10
	#for i in range(l):
	#	print(selector_list[i].name + "  " + str(times[i]))
	
	return times

def main():
	HS = s.HeapSelector()
	DS = s.DeterministicSelector()
	RS = s.RandomSelector()
	n = 100000
	k = range(1000,n//2+1,100)
	selector_list = [HS,DS,RS]
	times = np.zeros(shape = [len(selector_list), len(k)])
	for i in tqdm(range(len(k))):
		times[:, i] = testcases(selector_list, n, k[i])

	for i in range(len(selector_list)):
		plt.plot(k, times[i,:], label = selector_list[i].name)
	plt.legend()
	plt.show()


if __name__ == "__main__":
	main()