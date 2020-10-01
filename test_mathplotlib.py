#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 07:55:26 2019

@author: abehrens
"""

import numpy as np
import matplotlib.pyplot as plt


#Berechnungen
x = np.linspace(0, 10, 100) 
y1 = np.sin(x) 
y2 = np.sqrt(x) 

#darstellung
plt.subplot(211) 
plt.plot(y1, 'r') 
plt.subplot(212) 
plt.plot(y2, 'b--') 
plt.show()

