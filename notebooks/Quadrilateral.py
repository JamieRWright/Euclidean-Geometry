from notebooks import Functions
from notebooks import Shape
from notebooks import Functions

"""This is the quad class"""
class Quadrilateral(object):
	"""This is the class which describes the points A, B, C and D as a Quadrilateral"""
	def __init__(self, A, B, C, D, name):
		self.v1 = A
		self.v2 = B
		self.v3 = C
		self.v4 = D
		self.name = name

	def isCyclic(self):
		"""returns an ideal describing ABCD as a Cyclic Quadrilateral"""
		return cyclicQuadrilateral(self.v1, self.v2, self.v3, self.v4)

	def isParallelogram(self):
		"""returns an ideal describing ABCD as a Parallelogram"""
		return (parallel(self.v1, self.v2, self.v4, self.v3)
			+ parallel(self.v1, self.v4, self.v2, self.v3))