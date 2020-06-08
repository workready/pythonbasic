

class Rectangle:  
    def __init__(self, l, w):
        # Aqui estamos llamando a los setters (ver abajo)
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
            raise ValueError("El valor de length ha de ser mayor que 0")
        else:
            self._length = value
            
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("El valor de width ha de ser mayor que 0")
        else:
            self._width = value

# Esto implica que no ha de ser posible crear objeto con dimensiones negativas. 
try:
    newRectangle = Rectangle(-12, 10)   # <1>
except ValueError as e:
    print(e)

newRectangle = Rectangle(12, 10)
print(newRectangle.area)
print(newRectangle.perimeter)

newRectangle.width = 5
newRectangle.length = 8
print(newRectangle.area)
print(newRectangle.perimeter)

newRectangle.width = -10

