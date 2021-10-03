import Selection_Algorithms as sa

class Selector(object):
	def select(self, arr, k): #given an arry and k, give back the k-th biggest values back
		return self.select_func(arr,k)

class BubbleSelector(Selector):
	def __init__(self):
		self.select_func = sa.BubbleSelection
		self.name = "BubbleSelector"
		

class HeapSelector(Selector):
	def __init__(self):
		self.select_func = sa.HeapSelection
		self.name = "HeapSelector"

class DeterministicSelector(Selector):
	def __init__(self):
		self.select_func = sa.DeterministicSelection
		self.name = "DeterministicSelector"

class RandomSelector(Selector):
	def __init__(self):
		self.select_func = sa.RandomSelection
		self.name = "RandomSelector"
