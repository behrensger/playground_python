#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 07:59:21 2019

@author: abehrens
"""
import pandas as pd


daten = {'Name': ['Alex', "Benni", 'Claudia'], 'Alter': [19, 18, 21], 'Groesse': [183, 178, 163]} 
df = pd.DataFrame(daten, columns=['Name', 'Alter', 'Groesse'])
filename = 'daten.csv'

df.to_csv(filename) 
xf = pd.read_csv(filename)
print(df == xf) #klappt nicht richtig, noch mal Beispiele suchen, wie das mit dem CSV-Schreiben ist.

