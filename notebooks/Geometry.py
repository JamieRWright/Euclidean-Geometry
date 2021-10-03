
"""
Geometry
====================================
The core module of the Geometry Package
A static class which holds information about the geometry inputted
"""

class Geometry:
    """ This is Geometry! """
    points = {}
    triangles = {}
    circles = {}
    angles = {}
    lines = {}
    variableDistances = {}
    quadrilaterals = {}
    variables = set([])

    @staticmethod
    def line(points, name=None): 
        if name is None:
            # we come up with a new name not currently in use
            n = 1
            name = "L" + str(n)
            while name in Geometry.points:
                n += 1
                name = "L" + str(n)
        l = Line(points, name)
        Geometry.lines[name] = l
        return l

    @staticmethod
    def point(name=None):
        "Return a new point"
        if name is None:
            # we come up with a new name not currently in use
            n = 1
            name = "X" + str(n)
            while name in Geometry.points:
                n += 1
                name = "X" + str(n)
        x = Geometry.new_variable(name + "_x")
        y = Geometry.new_variable(name + "_y")
        p = Point(x, y, name)
        Geometry.points[name] = p
        return p
    
    @staticmethod
    def newRadius(name, value=None):
        varName = name
        n = 1
        while name in Geometry.variableDistances:
            varName = name+str(n)
            n += 1
        Geometry.new_variable(varName)
        r = Distance(varName, value)
        Geometry.variableDistances[varName] = r
        return r
    
    @staticmethod
    def circle(O, r, name=None):
        if name is None:
            # we come up with a new name not currently in use
            n = 1
            name = "C" + str(n)
            while name in Geometry.circles:
                n += 1
                name = "C" + str(n)
        c = Circle(O, r, name)
        Geometry.circles[name] = c
        return c

    @staticmethod
    def angle(B, A, C, name=None):
        if name is None:
            # come up with a new name not currently in use
            n = 1
            name = "A" + str(n)
            while name in Geometry.angle:
                n += 1
            tan = Geometry.newTan(name)
        else:
            tan = Geometry.newTan(name) 
        r = Geometry.getRing()
        a = Angle(B, A, C, tan, name)
        Geometry.angles[tan] = a
        return a
    
    @staticmethod
    def triangle(v1, v2, v3, name=None):
        "Return a triangle"
        if name is None:
            # come up with a new name not currently in use
            n = 1
            name = "T" + str(n)
            while name in Geometry.triangles:
                n += 1
                name = "T" + str(n)
        area_inv = Geometry.new_variable(name + "_area_inv")
        t = Triangle(v1, v2, v3, area_inv)
        Geometry.triangles[name] = t
        return t
    
    @staticmethod
    def quadrilateral(A, B, C, D, name=None):
        if name is None:
            # come up with a new name not currently in use
            n = 1
            name = "Q" + str(n)
            while name in Geometry.quadrilaterals:
                n += 1
                name = "Q" + str(n)
        q = Quadrilateral(A, B, C, D, name)
        Geometry.quadrilaterals[name] = q
        return q
    
    @staticmethod
    def getRing(coefficients="QQ"):
        "Gets the current ring in the geometry"
        return "PolynomialRing(coefficients, names=list(Geometry.variables))"
    
    
    @staticmethod
    def new_variable(name):
        Geometry.variables.add(name)
        return name
    
        
    def newDistance(name):
        varName = name
        n = 1
        while name in Geometry.variableDistances:
            varName = name+str(n)
            n += 1
        Geometry.new_variable(varName)
        return varName
    
    def newTan(name):
        varName = "tan_"+name
        n = 1
        while name in Geometry.angles:
            varName = "tan_"+name+n
            n += 1
        Geometry.new_variable(varName)
        return varName