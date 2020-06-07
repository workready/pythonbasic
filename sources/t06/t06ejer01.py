

class Rectangle:  
    pass # Tu codigo aqui
    
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

