#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 01:39:59 2019

@author: abehrens
"""

import numpy as np

#Arrays definieren
a = np.array([1,2,3,4])
b = np.array([(1,2,3,4), (6,7,8,9)], dtype=float)
c = np.array([
            [
                    (1,2,3,4),(5,6,7,8),(9,10,11,12)
            ],
            [
                    (1,2,3,4),(5,6,7,8),(9,10,11,12)
            ],
            [
                    (1,2,3,4),(5,6,7,8),(9,10,11,12)
            ]
            
        ])
d = np.full((1,2,3,4),1)
e = np.zeros((3,4), dtype=float)
f = np.ones((3,4), dtype=float)
g = np.empty((3,3))
h = np.random.random((3,4))

#Informationen über ein Array
print(b.shape)
print("Dim="+str(c.ndim)) #Anzahl Dimension
print("Size="+str(c.size)) #Anzahl Elemente
print("DType="+str(c.dtype)) #Element-Typ



#Rechnen mit Arrays
print(b)
print(b*2) #Sklaren
print(b+2)
print(b+b) #gleichgroßes Array
print(b*b) #gleichgroßes Array
print(b.sum())
print(b.min() + b.max())
print(b.mean())
print(np.median(b))

#Zugriff per Index
print(b[1,2] == 8)

print("\nIndex verändern")
print(b)
print(np.transpose(b))
print(b.ravel())


print("\n Speichern und Laden")
filename = 'b_array.npy'
filenamecsv = 'b_array.csv'
c = b
np.save(filename, b)
b = np.load(filename)
print(b == c)


np.savetxt(filenamecsv, b)
b = np.loadtxt(filenamecsv)
print(b == c)
