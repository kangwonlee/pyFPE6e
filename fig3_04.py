"""  Figure 3.4      Feedback Control of Dynamic Systems, 6e
                        Franklin, Powell, Emami
 script to generate Fig. 3.4
"""
## fig3_04.m    Example 3.5
import pylab as pl
import scipy.signal as ss

import control

pl.clf()
k = 1
num = 1  # form numerator
den = [1, k]  # form denominator
# sinusoidal input signal
deltaT = 0.001
t = pl.arange(0, 10 + deltaT * 0.5, deltaT)  # form time vector
u = pl.sin(10 * (t))  # form input
sys = ss.TransferFunction(num, den)  # form system
t_out, y_out, x_out = ss.lsim(sys, u, t)  # linear simulation
# plot response
pl.figure();
pl.plot(t_out, y_out);
pl.xlabel('Time (sec)');
pl.ylabel('Output');
pl.title('Fig. 3.4 (a): transient response')
pl.show()

pl.hold(True)
y1 = (10 / 101) * pl.exp(-t);
phi = pl.arctan(-10);
y2 = (1 / pl.sqrt(101)) * pl.sin(10 * t + phi);
pl.plot(t, y1, t, y2, t, y1 + y2);
# grid
control.nicegrid()
pl.show()

pl.hold(False)
pl.figure()
ii = pl.arange(9001, 10001)
pl.plot(t_out[ii], y_out[ii],
        t[ii], u[ii])

pl.xlabel('Time (sec)')
pl.ylabel('Output, input')
pl.title('Fig. 3.4 (b): Steady-state response')
pl.text(9.4, 0.65, 'u(t)')
pl.text(9.24, 0.12, 'y(t)')
# grid
control.nicegrid()

pl.show()
