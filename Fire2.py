# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:03:40 2016

@author: SRI' Kasturi
"""

from pyper import *
import matplotlib.pyplot as plt
burned_num = []
percentage = []
r = R(RCMD="C:\\Program Files\\R\\R-3.3.1\\bin\\x64\\R")
r('library(RNetLogo)')
r('nl.path <- "C:\\Program Files (x86)\\NetLogo 5.2.1"')
r('NLStart(nl.path, gui=TRUE)')
r('model.path <- "/models/Sample Models/Earth Science/Fire2.nlogo"')
r('NLLoadModel(paste(nl.path,model.path,sep=""))')

for i in range(1, 15):
   print( '------------------', i*5, '------------------------')
   percentage.append(i*5)
   r('NLCommand("set density ' + str(i*5) + '")')
   r('NLCommand("setup")')
   r('NLDoCommand(1000, "go")')
   r('burned <- NLReport("burned-trees")')
   print(r.burned)
   burned_num.append(r.burned)
plt.figure(figsize=(8,4))
plt.xlabel("Density")
plt.ylabel("Burned-trees")
plt.plot(percentage, burned_num)
plt.show()
r('NLQuit()')