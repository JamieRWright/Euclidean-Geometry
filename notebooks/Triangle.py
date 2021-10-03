from notebooks import Geometry
from notebooks import Functions
from notebooks import Shape

class Triangle(object):
    
    def __init__(self, v1, v2, v3, area_inv):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.area_inv = area_inv
        
    def makeEdges(self):
        e1 = Geometry.line([self.v1,self.v2])
        e2 = Geometry.line([self.v2,self.v3])
        e3 = Geometry.line([self.v3,self.v1])
        outEdges = [e1,e2,e3]
        return outEdges

    def area(self):
        r = Geometry.getRing()
        x1 = r(self.v1.x)
        y1 = r(self.v1.y)
        x2 = r(self.v2.x)
        y2 = r(self.v2.y)
        x3 = r(self.v3.x)
        y3 = r(self.v3.y)
        return (x2*y3 - x3*y2 + x3*y1 - x1*y3 + x1*y2 - x2*y1)/2
    
    def inTriangle(self, P):
        r = Geometry.getRing()
        A = self.v1
        B = self.v2
        C = self.v3
        PAB = Triangle(P, A, B, "P"+A.name+B.name)
        PBC = Triangle(P, B, C, "P"+B.name+C.name)
        PAC = Triangle(P, A, C, "P"+A.name+C.name)
        return r.ideal([self.area() - PAB.area() - PBC.area() - PAC.area()])

    
    def cevians(self, D, E, F, O):
        "Defines the three cevians AD, BE, and CF of triangle ABC with point O"
        DEF = Geometry.triangle(D, E, F)
        return (DEF.nondegenerate() 
            + collinear(A,O,D) 
            + collinear(B,O,E) 
            + collinear(C,O,F) 
            + self.edges[0].collinear(F) 
            + self.edges[1].collinear(D) 
            + self.edges[2].collinear(E))

    #Definitely a clever way of ordering classes to make this more natural
    #def generateCircumcircle(self, O, r):
    #    "Generates a new circumcircle"
    #    return Geometry.circle(O, r, self.name+"_circumcircle")

    def nondegenerate(self):
        r = Geometry.getRing()
        return r.ideal([self.area() * r(self.area_inv) - 1])
    
    def orthocentre(self, H):
        return orthocentre(H, self.v1, self.v2, self.v3)
    
    def circumcentre(self, O):
        return circumcentre(O, self.v1, self.v2, self.v3)
    
    def circumradius(self, a, b, c, r):
        ring = Geometry.getRing()
        #abc/(4*area) = circumradius
        sides = self.makeEdges()
        return (ring.ideal([4*self.area()*ring(r) - ring(a)*ring(b)*ring(c)])
                + sides[0].isDistance(a)
                + sides[1].isDistance(b)
                + sides[2].isDistance(c))
    
    def centroid(self, G):
        return centroid(G, self.v1, self.v2, self.v3)
     
    def ninePointCentre(self, N):
        return ninePointCentre(N, self.v1, self.v2, self.v3)
