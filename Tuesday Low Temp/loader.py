import numpy as np
import matplotlib.pyplot as plt
import sys

T, V, I, R = np.loadtxt("95k0.dat")

print T

files = []

for i in range(30):
    z = "95k" + str(i) + ".dat"
    Tz, Vz, Iz, Rz = np.loadtxt(z)
    T = np.append(T, Tz, axis=0)
    V = np.append(V, Vz, axis=0)
    I = np.append(I, Iz, axis=0)
    R = np.append(R, Rz, axis=0)
    files = np.append(files, z)
    print files

for n in range(30):
    x = str(n) + "952k.dat"
    Tx, Vx, Ix, Rx = np.loadtxt(x)
    T = np.append(T, Tx, axis=0)
    V = np.append(V, Vx, axis=0)
    I = np.append(I, Ix, axis=0)
    R = np.append(R, Rx, axis=0)
    files = np.append(files, x)
    print files

Ta, Va, Ia, Ra = np.loadtxt("autotest.dat")
T = np.append(T, Ta, axis=0)
V = np.append(V, Va, axis=0)
I = np.append(I, Ia, axis=0)
R = np.append(R, Ra, axis=0)
files = np.append(files, "autotest.dat")
print files

Tc, Vc, Ic, Rc = np.loadtxt("120k.dat")
T = np.append(T, Tc, axis=0)
V = np.append(V, Vc, axis=0)
I = np.append(I, Ic, axis=0)
R = np.append(R, Rc, axis=0)
files = np.append(files, "120k.dat")
print files

Td, Vd, Id, Rd = np.loadtxt("140k.dat")
T = np.append(T, Td, axis=0)
V = np.append(V, Vd, axis=0)
I = np.append(I, Id, axis=0)
R = np.append(R, Rd, axis=0)
files = np.append(files, "140k.dat")
print files

Te, Ve, Ie, Re = np.loadtxt("160k.dat")
T = np.append(T, Te, axis=0)
V = np.append(V, Ve, axis=0)
I = np.append(I, Ie, axis=0)
R = np.append(R, Re, axis=0)
files = np.append(files, "160k.dat")
print files

Tf, Vf, If, Rf = np.loadtxt("190k.dat")
T = np.append(T, Tf, axis=0)
V = np.append(V, Vf, axis=0)
I = np.append(I, If, axis=0)
R = np.append(R, Rf, axis=0)
files = np.append(files, "190k.dat")
print files

Tg, Vg, Ig, Rg = np.loadtxt("230k.dat")
T = np.append(T, Tg, axis=0)
V = np.append(V, Vg, axis=0)
I = np.append(I, Ig, axis=0)
R = np.append(R, Rg, axis=0)
files = np.append(files, "230k.dat")
print files

Th, Vh, Ih, Rh = np.loadtxt("250k.dat")
T = np.append(T, Th, axis=0)
V = np.append(V, Vh, axis=0)
I = np.append(I, Ih, axis=0)
R = np.append(R, Rh, axis=0)
files = np.append(files, "250k.dat")
print files

for p in range(11):
    t = "test" + str(p+1) + ".dat"
    Tt, Vt, It = np.loadtxt(t)
    Rt = Vt/It
    T = np.append(T, Tt, axis=0)
    V = np.append(V, Vt, axis=0)
    I = np.append(I, It, axis=0)
    R = np.append(R, Rt, axis=0)
    files = np.append(files, t)
    print files

for b in range(3):
    w = "testBig" + str(b+1) + ".dat"
    Tw, Vw, Iw = np.loadtxt(w)
    Rw = Vw/Iw
    T = np.append(T, Tw, axis=0)
    V = np.append(V, Vw, axis=0)
    I = np.append(I, Iw, axis=0)
    R = np.append(R, Rw, axis=0)
    files = np.append(files, w)
    print files

print files
print len(files)

lone = 3.338 - 1.336
ltwo = 3.340 - 1.338
lthree = 3.407 - 1.400
lfour = 3.410 - 1.392
lfive = 11.614-9.671
lsix = 12.759-10.734
l = np.average([lone, ltwo, lthree, lfour, lfive, lsix])

wone = 3.386 - 3.074
wtwo = 3.385 - 3.065
wthree = 6.218-6.036
wfour = 5.122-4.935
w = np.average([wone, wtwo,wthree,wfour])

done = 4.008 - 3.777
dtwo = 4.019 - 3.78
dthree = 6.476-6.216
dfour = 5.463-5.163
d = np.average([done, dtwo,dthree,dfour])

resist = abs((d*w/l)*R)
print resist

plt.figure()
plt.plot(T, resist, 'b',marker='x', linewidth=0)
plt.axvline(x=108)
plt.axvline(x=105)
plt.axvline(x=99)
plt.show()
