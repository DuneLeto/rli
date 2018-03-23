# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys, os, fnmatch

T, V, I, R = np.loadtxt("fifthsemi/0fifthsemi.dat")

ls = ["semi1", "semi2", "secondsemi", "semiup1", "fourthsemi", "fifthsemi"]
path = ls[0]
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, "*.dat"):
        filename = os.path.join(root, filename)
        Ta, Va, Ia, Ra = np.loadtxt(filename)
        T = np.append(T, Ta)
        V = np.append(V, Va)
        I = np.append(I, Ia)
        R = np.append(R, Ra)

T = abs(T)
V = abs(V)
I = abs(I)
R = abs(R)

plt.figure()
plt.plot(T, R, 'b',marker='x', linewidth=0)
plt.ylabel(u"R / Ω")
plt.xlabel(u"T / K")
plt.show()
