#!/usr/bin/env python3
import math
#import numpy


#preguntar por qué math.log no acepta tuplas
def f1(x):
    loga = math.log10(x)
    print ('LOG de', x ,'es', loga)
    return x
    #x = list(zip(*x))
    #x = zip(*x)
    
#f1(1)

x = (1000, 10000, 10, 234, 50)
for x in x:
    f1(x)
