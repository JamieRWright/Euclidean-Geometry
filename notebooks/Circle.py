from notebooks import Geometry
from notebooks import Functions
from notebooks import Shape
class Circle(object):
    
    def __init__(self, O, r, name):
        self.radius = r
        self.centre = O
        self.name = name
        
    def getName(self):
        return self.name
    
    def getCentre(self):
        return self.centre
    
    def getRadius(self):
        return self.radius
    
    def onCircle(self, P):
        "P lies on circle"
        r = Geometry.getRing()
        (ox, oy) = (r(self.centre.x), r(self.centre.y))
        return r.ideal([(r(P.x) - ox)^2 + (r(P.y) - oy)^2 - r(self.radius)^2])
    
    def isDiameter(self, P, Q):
        "PQ is the diameter of a circle"
        r = Geometry.getRing()
        (xP,yP) = P.toTuple()
        (xQ,yQ) = Q.toTuple()
        (xO,yO) = (r(self.centre.x), r(self.centre.y))
        return r.ideal([(r(yQ)-yO) - (yO-r(yP)), (r(xQ) - xO) - (xO - r(xP))]) +  self.onCircle(P)
    
    def powerOfPointCondition(self, A, B, C, D):
        return powerOfPointCondition(self, A, B, C, D)
    
    def circleIntersection(self, circle, P, Q):
        "self interects with circle at points P and Q"        
        r = Geometry.getRing()
        return r.ideal([self.onCircle(P)
                        +self.onCircle(Q)
                        +circle.onCircle(P)
                        +circle.onCircle(Q)])