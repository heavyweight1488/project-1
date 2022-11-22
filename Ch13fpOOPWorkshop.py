class Rectangle():
    
    def __init__(self, a, b):
        self.aSt = a
        self.bSt = b
        
    def callculator_perimeter(self):
       return 2 * (self.aSt + self.bSt)
   
        
class Square():
    
    def __init__(self, s1):
        self.s1 = s1
    
    def callculator_perimetr(self):
        return self.s1 * 4
    
rectangle = Rectangle(5, 5)
print('task1: ' + str (rectangle.callculator_perimeter()))

square = Square(10)
print('task1: ' + str (square.callculator_perimetr()))




class Square():
    
    def __init__(self, a):
        self.a = a
        
    def perSquare(self):
        return self.a * 4
    
    def changeSize(self, new_size):
        self.a += new_size
        
arSquare = Square(20)
print('task2: ' + str (arSquare.a))

arSquare.changeSize(4)
print('task 2: ' + str (arSquare.a))



class Shape():
    
    def what_am_i(self):
        print("я фигура!")
        
        
class Rectangle(Shape):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def calculate_perimetr(self):
        return 2 *(self.a + self.b)
    
    
class Square(Shape):
    
    def __init__(self, s1):
        self.s1 = s1
        
    def area(self):
        return self.s1 * 4
    
    
rectangle = Rectangle(5, 10)
square = Square(15)

print('task3: ' + str (rectangle.calculate_perimetr()))
rectangle.what_am_i()

print('task3: ' + str (square.area()))
square.what_am_i()


class horse():
    
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
        
class rider():
    
    def __init__(self, name):
        self.name = name
        
vladislav = rider("vladislav lomovoi")
lilia = horse("lilia", "arabian horse", vladislav)

print('task4: ' + str (lilia.owner.name))
    

    


    
        
        
    



