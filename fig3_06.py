#  Figure 3.6     Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
# script to generate Fig. 3.6
## fig3_06.m                                            
# Satellite Pulse response Example. 3.19 

import pylab as pl
import scipy.signal as ss

import control

pl.clf()
# transfer function
numG = [0, 0, 0.0002]
denG = [1, 0, 0]
sysG = ss.TransferFunction(numG, denG)
t = pl.arange(0, 10 + 0.005, 0.01)
# pulse input
u1 = pl.array(([0] * 500) + ([1] * 10) + ([0] * 491))
tout, yout, xout = ss.lsim(sysG, u1, t)
pl.figure(10)
pl.plot(t, u1)
pl.xlabel('Time (sec)')
pl.ylabel('Thrust Fc')
pl.title('Fig. 3.6(a): Thrust input')
pl.axis([0, 10, 0, 26])
# grid
control.nicegrid()
pl.show()

# conversion to degrees
ff = 180 / pl.pi
yout_deg = ff * yout
pl.figure(20)
pl.plot(t, yout_deg)
pl.xlabel('Time (sec)')
pl.ylabel('θ (deg)')
pl.title('Fig. 3.6(b): Satellite attitude')
# grid
control.nicegrid()
pl.show()
