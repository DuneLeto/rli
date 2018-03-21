# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:10:15 2016

@author: Aidan Hindmarch

Example script to run low temperature conductivity experiment.

Controls:
    Keithley 2000 series DMM
    Oxford Instruments Mercury iTC temperature controller
    Tenma 72-2550 PSU

"""
from __future__ import print_function, division
from level2labs.lowtemperature import K2000, MercuryITC, TenmaPSU
from time import sleep

import sys
import numpy
import pylab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Get required number of points and output filename from commandline
npts = int(sys.argv[1])
#savename = None
savename = sys.argv[2]

# Connect to devices
ITC = MercuryITC('COM3') # PI USB-to-serial connection COM3
t = ITC.modules[0] # module 0 is temperature board
#h = ITC.modules[1] # module 1 is heater power board

PSU = TenmaPSU('COM4') # USK-K-R-COM USB-to-serial connection COM4, must be connected via USB hub
#print(PSU.GetIdentity()) # Prints PSU device identity string to terminal

#National Instruments GPIB-USB-HS GPIB interface
Vdmm = K2000(16,0) # GPIB adaptor gpib0, device address 16
Vdmm.write(":SENS:FUNC 'VOLT:DC'") # configure to dc voltage
Idmm = K2000(26,0) # GPIB adaptor gpib0, device address 26
Idmm.write(":SENS:FUNC 'CURR:DC'") # configure to dc current


PSU.SetCurrent=0.01 #A
# write the PSU current setpoint (float, in Ampere units)
print('PSU current output set to {} A'.format(PSU.SetCurrent))
# read back PSU current setpoint value and print to terminal

temps = numpy.arange(95.0,110.,0.5)
# initialise data arrays
T = numpy.zeros((npts, len(temps)))
V = numpy.zeros((npts, len(temps)))
I = numpy.zeros((npts, len(temps)))
R = numpy.zeros((npts, len(temps)))

temp = t.tset
# read in the temperature setpoint. t.temp returns a tuple containing the latest
# temperature reading(float) as element 0 and unit(string) as element 1
print('Temperature at {} {}'.format(temp[0],temp[1])) # print to screen

# loop to take repeated readings
for i in range(len(temps)):
    t.tset = temps[i]
    temp = t.tset
    sleep(20)
    print('Temperature set to {:.2f} {}'.format(temp[0],temp[1])) # print to screen
    for p in range(npts):
        #PSU.SetCurrent=0.002*p #A - current ramp
	#	or
        #PSU.SetVoltage=0.05*p #V - voltage ramp

        sleep(1) # pause before taking readings
        T[p,i]=t.temp[0]
        # t.temp returns a tuple containing the latest temperature reading (float)
        # as element 0 and unit(string) as element 1
        V[p,i]=Vdmm.reading # *dmm.reading returns latest reading from *dmm (float, in Volt or Ampere units)
        I[p,i]=Idmm.reading
        R[p,i]=V[p,i]/I[p,i] # calculate resistance - note the __future__ division import...
        print(p, T[p,i], V[p,i], I[p,i], R[p,i]) # print to screen

        if not (savename==None):
            numpy.savetxt(str(i)+savename, (T[:,i],V[:,i],I[:,i],R[:,i])) # save data to file

    PSU.OutputOff	# Turn off PSU output


#t.tset = 100.0 # set temperture setpoint on ITC to next required value
temp=t.tset # read in the temperature setpoint
print('Temperature set to {} {}'.format(temp[0],temp[1])) # print to screen

#Disconnect from instruments
PSU.close()
ITC.close()

for i in temps:
# plot a graph
    plt.figure()
    gs = gridspec.GridSpec(2,2)

    ax0 = plt.subplot(gs[0,0])
    ax0.plot(T[:,i], R[:,i], '-k', marker='x')

    ax1 = plt.subplot(gs[1,0])
    plt.plot(I[:,i], V[:,i], '-b', marker='x')

    ax2 = plt.subplot(gs[0,1])
    plt.plot(I[:,i], R[:,i], '-r', marker='x')

    ax3 = plt.subplot(gs[1,1])
    plt.plot(V[:,i], R[:,i], '-r', marker='o')

    plt.show()
