"""% Fig. 2.15   Feedback Control of Dynamic Systems, 6e
             Franklin, Powell, Emami
"""
import pylab as pl
import scipy.signal as ss

# clear all;
# close all;
pl.close('all')

# g=9.81;     % m/sec^2
# L=1;        % m
# m=1;        % Kg
# r2d=57.295; % radians to degrees

g = 9.81  # m/sec/sec
L = 1.0  # m
m = 1.0  # Kg
r2d = 57.295  # radians to degrees

# num = 1/(m*L^2);
num = 1 / (m * L ** 2)
# den = [1 0 g/L];
den = [1, 0, g / L]
# t=0:.02:10;
t = pl.arange(0, 10 + 1e-6, 0.02)

sys = ss.TransferFunction(num, den)
# y = step(num,den,t);  % output in radians
tout, yout = ss.step(sys, T=t)
# plot(t,r2d*y),grid
pl.plot(tout, pl.degrees(yout))
pl.grid(True)

# xlabel('Time (sec)')
pl.xlabel('Time (sec)')
# ylabel('Pendulum angle \theta (deg)')
pl.ylabel('Pendulum angle \theta (deg)')
# title('Fig. 2.15')
pl.title('Fig. 2.15')
# nicegrid

pl.show()
