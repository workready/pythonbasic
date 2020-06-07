import math

class Circle:  
    pass    # Tu codigo aqui
  
NewCircle = Circle(8)  
print(NewCircle.area)  # 201.06192982974676
print(NewCircle.perimeter) # 50.26548245743669

NewCircle.radius = 5
print(NewCircle.area)  # 78.53981633974483
print(NewCircle.perimeter)  # 31.41592653589793

NewCircle.radius = -12  # El valor de radius ha de ser mayor que 0