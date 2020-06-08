import random

names = ["jorge", "bartola", "mariano"]
codes = ["mr.pink", "mr.white", "mr.blonde"]

def shuffle(a):
    random.shuffle(a)
    return a

print(dict(zip(names, shuffle(codes))))
