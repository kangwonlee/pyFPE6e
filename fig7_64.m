%  Figure 7.64      Feedback Control of Dynamic Systems, 6e
%                        Franklin, Powell, Emami
% script to generate Fig. 7. 64
% Robust Servo Example  
%% Example 7.36; Figure 7.64
clf;
clear all;
F=[0 1; 0 -1];
G=[0;1];
H=[1 0];
J=[0];
omega=1;
a=[0 1 0 0;-omega*omega 0 1 0;0 0 0 1;0 0 0 -1];
b=[0;0;G];

% desired closed-loop poles
pc=[-1+sqrt(3)*j;-1-sqrt(3)*j;-sqrt(3)+j;-sqrt(3)-j];
k=acker(a,b,pc);

% form controller matrices
k1=k(:,1:2);
ko=k(:,3:4);
ac=[0 1;-omega*omega 0];
bc=-[k(2);k(1)];;
cc=[1 0];
dc=[0];

% closed-loop system
acl=[F-G*ko G*cc;bc*H ac];
bcl=[0;0;-bc];
ccl=[H 0 0];
dcl=[0];
syscl=ss(acl,bcl,ccl,dcl);
pole(syscl)
tzero(syscl)
% blocking zeros
dcle=-1;
syse=ss(acl,bcl,ccl,dcle);
tzero(syse)
% Closed-loop response
t=0:.01:25;
r=sin(t);
y=lsim(syscl,r,t);
figure(1)
plot(t,y,t,r);
text(0.5,0.8,'r');
text(1.5,.4,'y');
xlabel('Time (sec)');
ylabel('Reference, output');
title('Fig. 7.64 (a): Tracking response');
nicegrid;

%Control effort
cclu=[-ko cc];
dclu=[0];
sysclu=ss(acl,bcl,cclu,dclu);
u=lsim(sysclu,r,t);
figure(2)
plot(t,u);
xlabel('Time (sec)');
ylabel('Control, u');
title('Fig. 7.64 (b): Control effort');
nicegrid

%error signal
ccle=[-H 0 0];
dcle=[1];
syscle=ss(acl,bcl,ccle,dcle);
e=lsim(syscle,r,t);
figure(3)
plot(t,e);
xlabel('Time (sec)');
ylabel('Error signal, e');
title('Fig. 7.64 (c): Tracking error');
nicegrid;



