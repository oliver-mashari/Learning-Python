# Line class exercise 1 
class Line:
    def __init__(self,coor1,coor2):
        self.x_coor1 = coor1[0]
        self.y_coor1 = coor1[1]
        self.x_coor2 = coor2[0]
        self.y_coor2 = coor2[1]
    
    def distance(self):
        distance = ((self.x_coor2 - self.x_coor1)**2 + (self.y_coor2 - self.y_coor1)**2)**0.5
        return distance 
    
    def slope(self):
        slope_m = (self.y_coor2 - self.y_coor1) / (self.x_coor2 - self.x_coor1)
        return slope_m

# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)

print("Distance:", li.distance())
print("Slope:", li.slope())

# Line class exercise 2
class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height 
        self.radius = radius

    def volume(self):
        volume = self.pi * ((self.radius)**2 ) * self.height 
        return volume 
    
    def surface_area(self):
        s_area = (2 * self.pi * self.radius * self.height) + (2 * self.pi * ((self.radius)**2))
        return s_area

# EXAMPLE OUTPUT
c = Cylinder(2,3)

print("Volume:",c.volume())
print("Surface Area:",c.surface_area())

# Homewrok solutions 
class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)