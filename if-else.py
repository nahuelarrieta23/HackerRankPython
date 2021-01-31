#!/bin/python3

import math
import os
import random
import re
import sys

def actions(n):
    txt = ''
    # Es impar si no es divisible por 2, es decir el resto es ditinto de 0
    if not n%2 == 0 : # Si es impar
        txt = 'Weird'
    if n%2==0 and 2<=n<=5:
        txt = 'Not Weird'
    if n%2==0 and 6<=n<=20:
        txt = 'Weird'
    if n%2==0 and n>20:
        txt = 'Not Weird'
    return txt
    

if __name__ == '__main__':

    n = int(input().strip())
    print(actions(n))