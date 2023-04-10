#frontier class

from heapq import heappush
from heapq import heappop

class priorityQueue:

	def __init__(self):
		self.heap = []
		#self.front = []

	def push(self, k):
		heappush(self.heap, k)
		

	def pop(self):
		return heappop(self.heap)

	def empty(self):
		if not self.heap:
			return True
		else:
			return False

