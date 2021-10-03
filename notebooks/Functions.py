from notebooks import Geometry
from notebooks import Point
"""
This is all the non class methods
"""
def centroid(G, A, B, C):
    """Generates the centroid G of triangle ABC"""
    r = Geometry.getRing()
    return r.ideal([r(A.x) + r(B.x) + r(C.x) - 3*r(G.x),
                    r(A.y) + r(B.y) + r(C.y) - 3*r(G.y)])

def orthocentre(H, A, B, C):
    """Generates the orthocentre H of triangle ABC"""
    return perpendicular(A, B, H, C) + perpendicular(A, C, H, B)

def circumcentre(O, A, B, C):
    """Generates the circumcentre O of triangle ABC"""
    r = Geometry.getRing()
    mAB = Point.midpoint(A, B, "mAB")
    mBC = Point.midpoint(B, C, "mBC")
    return rightAngle(A, mAB, O) + rightAngle(B, mBC, O)

def ninePointCentre(N, A, B, C):
    """Generates the 9 point centre N of triangle ABC"""
    r = Geometry.getRing()
    (xN, yN) = N.toTuple()
    (xA, yA) = A.toTuple()
    (xB, yB) = B.toTuple()
    (xC, yC) = C.toTuple()
    return r.ideal([4*xN*xA - 4*xN*xC + 4*yN*yA - 4*yN*yC - xA^2 - 2*xA*xB - yA^2 - 2*yA*yB + 2*xB*xC + 2*yB*yC + xC^2 + yC^2,
                                  4*xN*xB - 4*xN*xC + 4*yN*yB - 4*yN*yC - 2*xA*xB + 2*xA*xC - 2*yA*yB + 2*yA*yC - xB^2 - yB^2 + xC^2 + yC^2,
                                  4*yN*xA*yB - 4*yN*xA*yC - 4*yN*yA*xB + 4*yN*yA*xC + 4*yN*xB*yC - 4*yN*yB*xC - xA^2*xB + xA^2*xC - 2*xA*yA*yB + 2*xA*yA*yC + xA*xB^2 - xA*yB^2 - xA*xC^2 + xA*yC^2 + yA^2*xB - yA^2*xC + 2*yA*xB*yB - 2*yA*xC*yC - xB^2*xC - 2*xB*yB*yC + xB*xC^2 - xB*yC^2 + yB^2*xC + 2*yB*xC*yC])

def perpendicularFoot(D, A, P, Q):
    """D is the foot of the perpendicular from A to PQ"""
    return rightAngle(A, D, P) + rightAngle(A, D, Q) + collinear(P, D, Q)

def parallel(P1, Q1, P2, Q2):
    """P1Q1 is parallel to P2Q2"""
    r = Geometry.getRing()
    (p1x, p1y) = P1.toTuple()
    (q1x, q1y) = Q1.toTuple()
    (p2x, p2y) = P2.toTuple()
    (q2x, q2y) = Q2.toTuple()
    return r.ideal([(q1y-p1y)*(q2x-p2x) - (q2y-p2y)*(q1x-p1x)])

def collinear(P, Q, R):
    """P, Q, and R are collinear"""
    return parallel(P, R, Q, R)

def onCircle(P, O, r):
    """P lies on circle, centre O, radius r"""
    ring = Geometry.getRing()
    (px, py) = P.toTuple()
    (ox, oy) = O.toTuple()
    return ring.ideal([(px-ox)^2 + (py-oy)^2 - ring(r)^2])

def perpendicular(A, B, P, Q):
    """The lines AB and QR are perpendicular"""
    r = Geometry.getRing()
    return r.ideal([(r(Q.y)-r(P.y))*(r(A.y)-r(B.y)) + (r(A.x)-r(B.x))*(r(Q.x)-r(P.x))])

def rightAngle(P, Q, R):
    """The angle at PQR is a right angle"""
    return perpendicular(P, Q, Q, R)

def isAngleSum(a, b, c):
    """Angle a = angle b + angle c"""
    r = Geometry.getRing()
    try:
        tan_a = r(a.tan)
    except:
        tan_a = a
    try:
        tan_b = r(b.tan)
    except:
        tan_b = b
    try:
        tan_c = r(c.tan)
    except:
        tan_c = c
    return r.ideal([tan_a*(1-tan_b*tan_c) - tan_b - tan_c])

def isDistance(d, P, Q):
    """d is the distance from P to Q"""
    r = Geometry.getRing()
    return r.ideal([r(d.name)^2 - squareDistance(P,Q)])

def isMidpoint(M, P, Q):
    """Generates M as the midpoint of PQ"""
    r = Geometry.getRing()
    return r.ideal([2*r(M.x) - r(P.x) - r(Q.x), 2*r(M.y) - r(P.y) - r(Q.y)])

def powerOfPointCondition(circle, A, B, C, D, P):
    """Generates the conditions sufficient for the power of a point theorem for point P to hold"""
    u = Geometry.new_variable("u")
    v = Geometry.new_variable("v")
    r = Geometry.getRing()   
    if Line.isLine([A,B]) == None:
        AB = Geometry.line([A,B], A.name + B.name)
    else:
        AB = Line.isLine([A,B])
    if Line.isLine([C,D]) == None:
        CD = Geometry.line([C,D], C.name + D.name)
    else:
        CD = Line.isLine([C,D])
    return (circle.onCircle(A)
         + circle.onCircle(B) 
         + circle.onCircle(C) 
         + circle.onCircle(D) 
         + AB.collinear(P)
         + CD.collinear(P) 
         + r.ideal([r(u)*(r(A.x)-r(B.x)) - 1, r(v)*(r(C.x)-r(D.x)) - 1]))

def squareDistance(P, Q):
    """Gets the square distance of PQ"""
    (px, py) = P.toTuple()
    (qx, qy) = Q.toTuple()
    return (px-qx)^2 + (py-qy)^2

def cyclicQuadrilateral(A, B, C, D):
    """ABCD is a cyclic quadrilateral (opposite angles add to 180)"""
    r = Geometry.getRing()   
    xBA = r(B.x) - r(A.x)
    xCA = r(C.x) - r(A.x)
    xDB = r(D.x) - r(B.x)
    xDC = r(D.x) - r(C.x)
    yBA = r(B.y) - r(A.y)
    yCA = r(C.y) - r(A.y)
    yDB = r(D.y) - r(B.y)
    yDC = r(D.y) - r(C.y)
    return r.ideal([(yBA*xDB - yDB*xBA)*(xCA*xDC + yCA*yDC) - (yCA*xDC - yDC*xCA)*(xBA*xDB + yBA*yDB)])

def isAngleBisector(A, X, Y, Z):
    """AY bisects XAZ"""
    # By the cosine rule:
    #   cos(XAY) = (AX^2 + AY^2 - XY^2)/(2.AX.AY)
    #   cos(YAZ) = (AY^2 + AZ^2 - YZ^2)/(2.AY.AZ)
    # So we can express equal angles by saying
    #   AZ*(AX^2 + AY^2 - XY^2) = AX*(AY^2 + AZ^2 - YZ^2)
    AX2 = squareDistance(A,X)
    AY2 = squareDistance(A,Y)
    AZ2 = squareDistance(A,Z)
    XY2 = squareDistance(X,Y)
    YZ2 = squareDistance(Y,Z)
    return AZ2*(AX2+AY2-XY2)^2 - AX2*(AY2 + AZ2 - YZ2)^2