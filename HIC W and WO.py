# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:23:43 2023

@author: Nathan Lee
"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integ

#2 separate functions for modeling HIC with and without air bag
def H1(t):
    t1 = 25
    t2 = 75
    d = t2 - t1      #setting two times and the difference is d
    at = lambda t: ((22000/(((t-74)**2)+500))) #equation for a(t) with airbag
    at2, err = integ.quad (at, t, t+d) #integrating
    hic = (d*((1/d)*at2)**2.5)/1000 #HIC equation
    return hic

def H2(t):
    t1 = 25
    t2 = 75
    d = t2 - t1
    #equation for a(t) without airbag
    at = lambda t: ((16400/(((t-68)**2)+500)))+(1480/(((t-93)**2)+18))
    at2, err = integ.quad (at, t, t+d)#integrating
    hic = (d*((1/d)*at2)**2.5)/1000 #HIC equation
    return hic

xv = [t for t in range (160)] #arbitrary plot range that looks nice
yv = [H1(t) for t in xv]

plt.figure()
plt.title("HIC with Airbag")
plt.plot(xv,yv)


xv = [t for t in range (160)]   #arbitrary plot range that looks nice
yv = [H2(t) for t in xv]

plt.figure()
plt.title("HIC without Airbag")
plt.plot(xv,yv)