%  Figure 3.35b      Feedback Control of Dynamic Systems, 6e
%                        Franklin, Powell, Emami
% script to generate Fig. 3.35(b)

clf;
num=1;
a=5;

zeta =1;
den2=[1/(zeta*a) 1];
den1=[1 2*zeta 1];
den=conv(den1,den2);
t=0:.1:10;
y1=step(num,den,t);

zeta =.7;
den2=[1/(zeta*a) 1];
den1=[1 2*zeta 1];
den=conv(den1,den2);
y2=step(num,den,t);

zeta =.5;
den2=[1/(zeta*a) 1];
den1=[1 2*zeta 1];
den=conv(den1,den2);
y3=step(num,den,t);

axis([0 5 .1 .9])
plot(t,y1,'-',t,y2,'--',t,y3,'-.'),
title('Fig. 3.35b Step response with extra pole, \alpha= 5')
xlabel('\omega_n t')
ylabel('y(t)')
% grid
nicegrid