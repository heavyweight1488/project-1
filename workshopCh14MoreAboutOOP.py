class Square():
    square_list = []
    
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append((self.width, self.len))
        
    def print_size(self):
        print("""{} на {}""".format(self.width, self.len))
        
        
sq1 = Square(1, 1)
sq2 = Square(2, 2)

print('task1: ' + str (Square.square_list))


class Square():
    
    def __init__(self, a):
        self.ast = a
        
        
    def print_size(self):
        return(""" {} на {} на {} на {}
              """.format(self.ast, self.ast, self.ast, self.ast))
        
sq = Square(5)
print('task2: ' + str (sq.print_size()))


class func:
    def __init__(self):
        self.name = 'vladislav'
        self.surname = 'lomovoi'
        
vladislav = func()
same_vlad = vladislav
print('task3: ' + str (vladislav is same_vlad))

another_vlad = func()
print('task3: ' + str (vladislav is another_vlad))
        
        


    