import pdb

def debug_this(i1, i2):
    result = i1
    pdb.set_trace() # Va a parar aqui
    for i in range(5):
        result += i2
    return result

result = debug_this(10, 20)