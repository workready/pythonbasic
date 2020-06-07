#-*- coding: utf-8 -*-
a = [1,2,3]
b = ['a','b','c','d']

print(list(zip(a,b)))

# Esto en Python 2 funcionaría, pero en Python 3 da error
#print(list(map(None,a,b)))