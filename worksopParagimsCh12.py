class Apple:
    
    
    def __init__(self, w, c, ss, si ):
        self.weight = w
        self.color = c
        self.sourSweet = ss
        self.size = si
        print('task1 :' + str ("create!"))
        

apple1 = Apple(2, "green", "sour", "small" )
apple2 = Apple(2, "yellow", "sweet", "small")
apple3 = Apple(4, "red", "sour-sweet", "big")
apple4 = Apple(5, "green", "sweet", "big")



from math import pi

class Circle:
    
    def __init__(self, r):
        self.radius = r
            
    def area(self):
        return 2 * pi * self.radius
    

circle = Circle(10)
print('task2: ' + str (circle.area()))




class Triangle:
    
    def __init__(self, r, a, b, c):
        self.radius = r
        self.aStorona = a
        self.bStorona = b
        self.cStorona = c
    
    def areaTriangle(self):
        return self.radius * (self.aStorona + self.bStorona + self.cStorona)
    

triangle = Triangle(2, 4, 8, 12)
print('task3: ' + str (triangle.areaTriangle()))


class Hexagon:
    
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.a1St = a1 
        self.a2St = a2
        self.a3St = a3
        self.a4St = a4
        self.a5St = a5
        self.a6St = a6
        
    def areaHexagon(self):
        return self.a1St + self.a2St + self.a3St + self.a4St + self.a5St + self.a6St
    
hexagon = Hexagon(2, 4, 6, 8, 10, 12)
print('task4: ' + str (hexagon.areaHexagon()))
        
    




