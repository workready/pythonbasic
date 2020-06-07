class Shape:
    pass # Tu codigo aqui
        

class Rectangle(Shape):  
    pass # Tu codigo aqui
            

newRectangle = Rectangle(12, 10)  
print(newRectangle.area)    # 120
print(newRectangle.perimeter)   # 44

newRectangle.width = 5
newRectangle.height = 8
print(newRectangle.area)    # 60
print(newRectangle.perimeter)   # 34

newRectangle.width = -10    # El valor de width ha de ser mayor que 0
