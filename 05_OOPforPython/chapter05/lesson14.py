class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass

    def get_area(self):
        return self.length * self.width 

    def get_perimeter(self):
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.width = length
        pass
        
        
