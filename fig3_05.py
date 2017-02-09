"""  Figure 3.5      Feedback Control of Dynamic Systems, 6e
                        Franklin, Powell, Emami
 script to generate Fig. 3.5
"""
## fig3_05.m
# Example 3.17 : DC Motor Angular velocity 

import pylab as pl
import scipy.signal as ss

import control


pl.clf()
numb = [0.0, 0.0, 100]
denb = [1, 10.1, 101]
sysb = ss.TransferFunction(numb, denb)
t = pl.arange(0, 5+0.005, 0.01)
tout, yout = ss.step(sysb, T=t)
pl.plot(tout, yout)
pl.title('Fig. 3.5: Step response')
pl.xlabel('Time (sec)')
pl.ylabel('ω (rad/sec)')
# grid
control.nicegrid()

pl.show()
