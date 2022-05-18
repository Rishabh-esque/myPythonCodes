class cube:
    def __init__(self,length):
        self.length = length
    
    def surface_area(self):
        return 6*self.length*self.length

    def volume(self):
        return self.length**3
    
    
    
c1 = cube(3)
print(c1.surface_area())
print(c1.volume())