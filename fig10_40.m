%  Figure 10.40      Feedback Control of Dynamic Systems, 6e
%                        Franklin, Powell, Emami
%
% fig9_40.m is a script to generate Fig. 10.40, the root locus
% of the aircraft with feedback from pitch rate to elevator
clf;
% aircraft system matrices
f=[-.00643 .0263 0 -32.2 0;
-.0941 -.624 820 0 0;
-.000222 -0.00153 -.668 0 0;
0 0 1 0 0;
0 -1 0 830 0];

g=[0; -32.7; -2.08; 0; 0];
h=[0 0 -1 0 0];
j=0;
%
%[np, dp]= ss2tf(f,g,h,j);
sys=ss(f,g,h,j);
% axis([-.02 .02 -.015 .015])
h1=figure;
rlocus(sys)
grid on;
title('Fig. 10.40: Root locus for pitch rate to elevator')
% now zoom in to origin
h3=axes('pos',[.1 .15 .35 .35]);
set(h1,'CurrentAxes',h3);
hold on;
rlocus(sys);
axis([-.02 0.01 -.12 .12]);
