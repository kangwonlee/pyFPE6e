#  Figure 3.7      Feedback Control of Dynamic Systems, 6e
#                        Franklin, Powell, Emami
# script to generate Fig. 3.7
# fig3_07.m                                          
# Satellite Double-Pulse Response Example 3.19

import pylab as pl
import scipy.signal as ss

import control

pl.clf()
dI = 1. / 5000
numG = dI
denG = [1, 0, 0]
sys = ss.TransferFunction(numG, denG)
t = pl.arange(0, 10 + 0.005, 0.01)
# pulse input
u2 = pl.array(([0] * 500) + ([25] * 10) + ([0] * 100) + ([-25] * 10) + ([0] * 381))
tout, yout, xout = ss.lsim(sys, u2, t)
pl.figure()
pl.plot(t, u2)
pl.axis([0, 10, -26, 26])
pl.xlabel('Time (sec)')
pl.ylabel('Thrust Fc')
pl.title('Fig. 3.7(a): Thrust input')
# grid
control.nicegrid()
pl.show()
# conversion to degrees
ff = 180 / pl.pi
y2 = ff * yout
pl.figure()
pl.plot(t, yout)
pl.xlabel('Time (sec)')
pl.ylabel('\theta (deg)')
pl.title('Fig. 3.7(b): Satellite attitude')
# grid
control.nicegrid()
pl.show()
