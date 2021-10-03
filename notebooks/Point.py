from notebooks import Geometry
class Point(object):
    """This is the Point class"""
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
    def toTuple(self):
        r = Geometry.getRing()
        return (r(self.x), r(self.y))
    
    #Getters
    def getX(self):
        return self.x
    def getY(self):
        return self.y   
    def getName(self):
        "Perhaps add a set name?"
        return self.name
    def isMidpoint(self, A, B):
        return isMidpoint(self, A, B)
    
    @staticmethod
    def toPoint(Tuple, name):
        x = Tuple[0]
        y = Tuple[1]
        p = Point(x, y, name)
        Geometry.points[name] = p
        return p

    @staticmethod
    def midpoint(A, B, name):
        r = Geometry.getRing()
        p = Point.toPoint(((r(A.x)+r(B.x))/2, (r(A.y)+r(B.y))/2), name)
        return p

    def fix(self, x, y):
        "Give real coordinates for a point"
        r = Geometry.getRing(coefficients = RR)
        return r.ideal([r(self.x) - x, r(self.y) - y])