"""  Figure 3.3      Feedback Control of Dynamic Systems, 6e
                        Franklin, Powell, Emami
 script to generate Fig. 3.3
 fig3_03.m Example 3.4
"""
import pylab as pl
import scipy.signal as ss

import control

# Frequency response
pl.clf()
k = 1
num = 1  # form numerator
den = [1, k]  # form denominator
sys = ss.TransferFunction(num, den) # form system
# frequency range
w = pl.logspace(-2, 2)

mag, phase = control.bode(sys, w)   # compute frequency response
# plot frequency response
pl.subplot(2, 1, 1)
pl.loglog(w, mag)
pl.xlabel('ω (rad/sec)')
pl.ylabel('M')
pl.title('Figure 3.3: Magnitude, phase')
pl.grid(True)
pl.subplot(2, 1, 2)
pl.semilogx(w, phase)
pl.xlabel('ω (rad/sec)')
pl.ylabel('φ (deg)')
pl.grid(True)
# Bode grid
control.bodegrid()                  # y grid to 70% gray solid

pl.show()
