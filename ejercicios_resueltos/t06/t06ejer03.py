class Shape:
    @property
    def area():
        raise NotImplementedError("Por favor, implementa este método en una clase hija")
        
    @property
    def perimeter():
        raise NotImplementedError("Por favor, implementa este método en una clase hija")
        

class Rectangle(Shape):  
    def __init__(self, l, w):  
        self.length = l  
        self.width  = w  
  
    @property
    def area(self):  
        return self._length*self._width
    
    @property
    def perimeter(self):
        return self._length * 2 + self._width * 2
    
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width
    
    @length.setter
    def length(self, value):
        if value < 0:
            print("El valor de length ha de ser mayor que 0")
        else:
            self._length = value
            
    @width.setter
    def width(self, value):
        if value < 0:
            print("El valor de width ha de ser mayor que 0")
        else:
            self._width = value
            

newRectangle = Rectangle(12, 10)  
print(newRectangle.area)    # 120
print(newRectangle.perimeter)   # 44

newRectangle.width = 5
newRectangle.height = 8
print(newRectangle.area)    # 60
print(newRectangle.perimeter)   # 34

newRectangle.width = -10    # El valor de width ha de ser mayor que 0
