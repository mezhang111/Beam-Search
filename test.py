import Selector as s
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pandas as pd
from tqdm import tqdm

def test_with_time_measure(selector, arr, k):
	start = time.time()
	res = selector.select(arr,k)
	end = time.time()
	return (end-start), res

def testcases(selector_list, n, k):
	l = len(selector_list)
	times = np.zeros(shape = [l])
	arr = np.random.normal(0,100,n)
	vals = np.empty(shape = l)
	for j in range(l):
		t, res = test_with_time_measure(selector_list[j],arr,k)
		times[j] = t 
		vals[j] = res
	for j in range(l-1):
		assert vals[j] == vals[j+1] #check if the results agree with each other
	
	return times

def plot(df, xlabel, ylabel, hue_label):
	sns.set(font_scale = 0.5)
	sns.pointplot(xlabel, ylabel, hue = hue_label, 
		data = df, dodge = True, join = False)
	plt.show()



def main():
	random.seed(112)
	np.random.seed(259)
	HS = s.HeapSelector()
	DS = s.DeterministicSelector()
	RS = s.RandomSelector()
	n = 100000
	k = [2**x for x in range(16)]
	selector_list = [HS,DS,RS]
	reps = 10
	l = len(selector_list)
	times = np.empty(shape = [len(k)*reps*l])

	for i in tqdm(range(len(k))):
		for j in range(reps):
			curr_index = i*reps*l + j*l
			times[curr_index: curr_index+l] = testcases(selector_list, n, k[i])

	logks = np.log2(np.repeat(k, reps*l))
	selector_names = [selector.name for selector in selector_list]*(len(k)*reps)
	df = pd.DataFrame({'logk': logks, 'time': times, 'selector': selector_names})
	plot(df, 'logk', 'time', 'selector')
	

if __name__ == "__main__":
	main()