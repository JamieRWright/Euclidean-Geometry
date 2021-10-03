from notebooks import Geometry
from notebooks import Functions

class Angle(object):
       
    def __init__(self, A, B, C, tanVar, name):
        self.v1 = A
        self.v2 = B
        self.v3 = C
        self.tan = tanVar
        self.name = name
 
    def getName(self):
        "Perhaps add a set name?"
        return self.name

    def getTanName(self):
        "Perhaps add a set name?"
        return self.tan
    
    def tangent(self):
        r = Geometry.getRing()
        (xA, yA) = self.v1.toTuple()
        (xB, yB) = self.v2.toTuple()
        (xC, yC) = self.v3.toTuple()
        
        # xBA = change in x for line of BA etc.
        yBA = (r(yB) - r(yA))
        xBA = (r(xB) - r(xA))
        yCB = (r(yC) - r(yB))
        xCB = (r(xC) - r(xB))
        return r.ideal([r(self.tan)*(xBA*xCB + yBA*yCB) + yCB*xBA - yBA*xCB])
    
    def isEqual(self, other):
        r = Geometry.getRing()
        return r.ideal([r(self.tan) - r(other.tan)])
    
    def isRightAngle(self):
        "The angle at PQR is a right angle"            
        return rightAngle(self.v1, self.v2, self.v3)
    
    def isHalfAngle(self, P):
        "Self is a half angle of P"
        return isAngleSum(P, self, self)
    
    def isPythagoras(self):
        r = Geometry.getRing()
        (xA, yA) = self.v1.toTuple()
        (xB, yB) = self.v2.toTuple()
        (xC, yC) = self.v3.toTuple()
        return r.ideal([(xB-xC)^2 + (yB-yC)^2 + (xA-xB)^2 + (yA-yB)^2 - (xA-xC)^2 - (yA-yC)^2])
