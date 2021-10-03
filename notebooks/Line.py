from notebooks import Geometry
from notebooks import Functions

class Line(object):
    def __init__(self, inPoints, name):
        self.points = inPoints
        self.name = name
        self.tan = None
        #self.distance = None ?
        
    def getPoint(self, i):
        if i > len(self.points):
            return "Error please enter a number less than or equal to "+str(len(self.points))
        else:
            return self.points[i]
    

    def tangent(self):
        if self.tan == "":
            self.tan = Geometry.newTan(name)            
        r = Geometry.getRing()
        A = self.getPoint(0)
        B = self.getPoint(1)
        return r.ideal([r(B.y) - r(A.y) - r(self.tan)*(r(B.x)-r(A.x))])
    
    def collinear(self, inPoint):
        return collinear (self.getPoint(0), inPoint, self.getPoint(1))

    def perpendicular(self, inLine):
        return perpendicular(self.getPoint(0), self.getPoint(1), inLine.getPoint(0), inLine.getPoint(1))
    
    def parallel(self, inLine):
        return parallel(self.getPoint(0), self.getPoint(1), inLine.getPoint(0), inLine.getPoint(1))
    
    def squareDistance(self):
        return squareDistance(self.points[-1], self.points[0])

    def perpendicularFoot(self, D, A):
        "D is the foot"
        return perpendicularFoot(D, A, self.getPoint(0), self.getPoint(1))
    
    def midpoint(M):
        return isMidpoint(M, self.getPoint(0), self.getPoint(1))
        
    def isDistance(self, d):
        "d is the distance from P to Q"
        r = Geometry.getRing()
        return r.ideal([(r(d))^2 - self.squareDistance()])
    
    def isTangent(self, point, circle):
        return self.perpendicularFoot(point, circle.centre) + circle.onCircle(Point)
        
    @staticmethod
    def isLine(inPoints):
        "Searches if a line already exists"
        outLine = None
        for x in Geometry.lines.values():
            if inPoints == x.points:
                outLine = x 
        return outLine
    