# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:04:33 2023

@author: Nathan Lee
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#ERU variables constant
erudoctors = 10
erunurses = 20
beds = 50
#ICU variables constant
icudoctors = 10
icunurses = 20
respirators = 30
#Seting inflow Rate of patients
def qin(t):
    inflow = 1
    return inflow
    #Hospital as a whole can be a function with two units
def hospital (space, t):
    #Outflow of each unit
    qout1 = min(1/7*space[0]*beds, erunurses, erudoctors)
    qout2 = min(1/20*space[1]*respirators, icunurses, icudoctors)
    #Differental equations for patients in both units
    dhdt1 = (qin(t) - qout1)/beds
    #changing the number in the equation below saturates another unit
    dhdt2 = (qin(t)*0.5 - qout2)/respirators
    
#states for defining overflow
    if space[0] >= 1 and dhdt1 >= 0:
        dhdt1 =0
    if space[1] >= 1 and dhdt2 >= 0:
        dhdt2 =0
         
    dhdt = [dhdt1,dhdt2]
    return dhdt
#initial state
state0 =[0,0]
#time step for simulation
t = np.linspace(0,365,1000)

#solves differential equation
states = odeint(hospital, state0, t)

#getting numbers of patients in ICU and ERU
eru_patients = states [:,0]*beds
icu_patients = states [:,1]*respirators

#plotting results and labeling
plt.plot(t, eru_patients, label='ERU')
plt.plot(t, icu_patients, label='ICU')
plt.xlabel("Time(Days)")
plt.ylabel("Patients")
plt.legend()