from notebooks import Geometry
import Functions

class Distance(object):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        
    def fix(self, value):
        r = Geometry.getRing()
        if self.value == None:
            self.value = value
        return r.ideal([r(self.name) - self.value])