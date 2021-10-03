import Geometry
import Functions
import Shape

class Quadrilateral(Shape):
    def __init__(self, A, B, C, D, name):
        self.v1 = A
        self.v2 = B
        self.v3 = C
        self.v4 = D
        self.name = name
        
    def isCyclic(self):
        return cyclicQuadrilateral(self.v1, self.v2, self.v3, self.v4)
    
    def isParallelogram(self):
        return (parallel(self.v1, self.v2, self.v4, self.v3) 
                + parallel(self.v1, self.v4, self.v2, self.v3))