import math

class Circle:  
    def __init__(self, r):  
        self.radius = r  
  
    @property
    def area(self):  
        return self._radius**2*math.pi  
      
    @property
    def perimeter(self):  
        return 2*self._radius*math.pi
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("El valor de radius ha de ser mayor que 0")
        else:
            self._radius = value
  
NewCircle = Circle(8)  
print(NewCircle.area)  # 201.06192982974676
print(NewCircle.perimeter) # 50.26548245743669

NewCircle.radius = 5
print(NewCircle.area)  # 78.53981633974483
print(NewCircle.perimeter)  # 31.41592653589793

NewCircle.radius = -12  # El valor de radius ha de ser mayor que 0