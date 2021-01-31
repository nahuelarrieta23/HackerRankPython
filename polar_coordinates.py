import sys
import cmath

def toPolar(z):
    comp = complex(z)
    mod = abs(comp)
    arg = cmath.phase(comp)
    return round(mod,3),round(arg,3)

z = input()
mimod, miph = toPolar(z)
print(mimod)
print(miph)
