s=xlsread('cast.xls');
ls=length(s);
plot(s)
[C,L] = wavedec(s,3,'db2');%执行3层信号分解，wavedec是多层分解函数
cA3 = appcoef(C,L,'db2',3);%从C中抽取3层近似系数，detcoef细节系数抽取，appcoef近似系数抽取
cD3 = detcoef(C,L,3);%从C中抽取3、2、1层细节系数
cD2 = detcoef(C,L,2);
cD1 = detcoef(C,L,1);
A3 = wrcoef('a',C,L,'db2',3);%从C中重建3层近似，waverec全重构，wrcoef有选择性重构，upcoef单一重构
D1 = wrcoef('d',C,L,'db2',1);%从C中重建1、2、3层细节系数
D2 = wrcoef('d',C,L,'db2',2);
D3 = wrcoef('d',C,L,'db2',3);
subplot(2,2,1); plot(A3);%显示3层分解的结果
title('Approximation A3')
subplot(2,2,2); plot(D1);
title('Detail D1')
subplot(2,2,3); plot(D2);
title('Detail D2')
subplot(2,2,4); plot(D3);
title('Detail D3')
[thr,sorh,keepapp]=ddencmp('den','wv',s);
T1=thr
%软硬阈值去噪重构
cd1soft1=wthresh(cD1,'s',T1);
cd2soft1=wthresh(cD2,'s',T1);
cd3soft1=wthresh(cD3,'s',T1);
sc1=[cA3',cd3soft1',cd2soft1',cd1soft1']';
s1=waverec(sc1,L,'db2');
%整体硬阈值去噪
cd1hard1=wthresh(cD1,'h',T1(1));
cd2hard1=wthresh(cD2,'h',T1(1));
cd3hard1=wthresh(cD3,'h',T1(1));
hc1=[cA3',cd3hard1',cd2hard1',cd1hard1']';
h1=waverec(hc1,L,'db2');
%y3阈值函数去噪
x3=length(cD3);
a=1;%参数
n=3;%参数
for i=1:x3
if abs(cD3(i))>=T1 
    l=abs(cD3(i))-T1;
    u=1-exp((-a)*(l.^2));
    h=(2*T1)/(1+exp(l.^n));
    ay3(i)=u*cD3(i)+(1-u)*sign(cD3(i))*(abs(cD3(i))-h);
else
   ay3(i)=0;
end;
end;
x2=length(cD2);
for i=1:x2
if abs(cD2(i))>=T1 
    l=abs(cD2(i))-T1;
    u=1-exp((-a)*(l.^2));
    h=(2*T1)/(1+exp(l.^n));
    ay2(i)=u*cD2(i)+(1-u)*sign(cD2(i))*(abs(cD2(i))-h);
else
    ay2(i)=0;
end;
end;
x1=length(cD1);
for i=1:x1
if abs(cD1(i))>=T1 
    l=abs(cD1(i))-T1;
    u=1-exp((-a)*(l.^2));
    h=(2*T1)/(1+exp(l.^n));
    ay1(i)=u*cD1(i)+(1-u)*sign(cD1(i))*(abs(cD1(i))-h);
else
    ay1(i)=0;
end;
end;
C1=[cA3',ay3,ay2,ay1];
W= waverec(C1,L,'db2');%从C中重建3层近似，waverec全重构，
%y4阈值函数
k=2/3;%y4的参数
n1=1;%y4的参数
m=1;%y4的参数
for i=1:x3
if abs(cD3(i))>=T1
    by3(i)=cD3(i)-((T1*k*sign(cD3(i)))/(exp((abs(cD3(i))-T1)/n1)));
else
    by3(i)=(m*((cD3(i))^(2*n1+1)))/((2*n1)*(T1^(2*n1)));
end;
end;
for i=1:x2
if abs(cD2(i))>=T1
    by2(i)=cD2(i)-((T1*k*sign(cD2(i)))/(exp((abs(cD2(i))-T1)/n1)));
else
    by2(i)=(m*((cD2(i))^(2*n1+1)))/((2*n1)*(T1^(2*n1)));
end;
end;
for i=1:x1
if abs(cD1(i))>=T1
    by1(i)=cD1(i)-((T1*k*sign(cD1(i)))/(exp((abs(cD1(i))-T1)/n1)));
else
    by1(i)=(m*((cD1(i))^(2*n1+1)))/((2*n1)*(T1^(2*n1)));
end;
end;
C2=[cA3',by3,by2,by1];
W2= waverec(C2,L,'db2');
%y5阈值函数
t0=2;%y5的中间阈值
k1=1;%y5的参数
for i=1:x3
if abs(cD3(i))>=T1
   l1=((abs(cD3(i)))-T1)/2;
    u1=2*k1+1;
    th1=u1*(1+exp(l1));
    m1=abs(cD3(i)); 
    cy3(i)=(sign(cD3(i)))*(m1-((2*T1)/th1));
elseif abs(cD3(i))<t0
    cy3(i)=0;
else
    cy3(i)=(k1*((cD3(i))^(2*k1+1)))/((2*k1+1)*(T1^(2*k1)));
end;
end;
for i=1:x2
if abs(cD2(i))>=T1
   l1=((abs(cD2(i)))-T1)/2;
    u1=2*k1+1;
    th1=u1*(1+exp(l1));
    m1=abs(cD2(i)); 
    cy2(i)=(sign(cD2(i)))*(m1-((2*T1)/th1));
elseif abs(cD2(i))<t0
    cy2(i)=0;
else
    cy2(i)=(k1*((cD2(i))^(2*k1+1)))/((2*k1+1)*(T1^(2*k1)));
end;
end;
for i=1:x1
if abs(cD1(i))>=T1
   l1=((abs(cD1(i)))-T1)/2;
    u1=2*k1+1;
    th1=u1*(1+exp(l1));
    m1=abs(cD1(i)); 
    cy1(i)=(sign(cD1(i)))*(m1-((2*T1)/th1));
elseif abs(cD1(i))<t0
    cy1(i)=0;
else
    cy1(i)=(k1*((cD1(i))^(2*k1+1)))/((2*k1+1)*(T1^(2*k1)));
end;
end;
C3=[cA3',cy3,cy2,cy1];
W3= waverec(C3,L,'db2');
%新阈值函数
t0=T1;%参数
k1=1;%参数
t1=1.9*T1;%参数
for i=1:x3
if abs(cD3(i))>=t1
   l1=((abs(cD3(i)))-T1)/2;
    u1=k1+1;
    h2=exp((abs(cD3(i)))-t1)*u1*(1+exp(l1));
    m1=abs(cD3(i)); 
    gcy3(i)=(sign(cD3(i)))*(m1-((2*T1)/h2));
elseif abs(cD3(i))<t0
    gcy3(i)=(k1*((cD3(i))^(2*k1+1)))/((k1+1)*(T1^(2*k1)));
else
    l1=((abs(cD3(i)))-T1)/2;
    u1=k1+1;
    h2=u1*(1+exp(l1));
    m1=abs(cD3(i)); 
    gcy3(i)=(sign(cD3(i)))*(m1-((2*T1)/h2));
end;
end;
for i=1:x2
if abs(cD2(i))>=t1
   l1=((abs(cD2(i)))-T1)/2;
    u1=k1+1;
    h2=exp((abs(cD2(i)))-t1)*u1*(1+exp(l1));
    m1=abs(cD2(i)); 
    gcy2(i)=(sign(cD2(i)))*(m1-((2*T1)/h2));
elseif abs(cD2(i))<t0
    gcy2(i)=(k1*((cD2(i))^(2*k1+1)))/((k1+1)*(T1^(2*k1)));
else 
    l1=((abs(cD2(i)))-T1)/2;
    u1=k1+1;
    h2=u1*(1+exp(l1));
    m1=abs(cD2(i)); 
    gcy2(i)=(sign(cD2(i)))*(m1-((2*T1)/h2));
end;
end;
for i=1:x1
if abs(cD1(i))>=t1
   l1=((abs(cD1(i)))-T1)/2;
    u1=k1+1;
     h2=exp((abs(cD1(i)))-t1)*u1*(1+exp(l1));
    m1=abs(cD1(i)); 
   gcy1(i)=(sign(cD1(i)))*(m1-((2*T1)/h2));
elseif abs(cD1(i))<t0
    gcy1(i)=(k1*((cD1(i))^(2*k1+1)))/((k1+1)*(T1^(2*k1)));
else
    l1=((abs(cD1(i)))-T1)/2;
    u1=k1+1;
    h2=u1*(1+exp(l1));
    m1=abs(cD1(i)); 
    gcy1(i)=(sign(cD1(i)))*(m1-((2*T1)/h2));
end;
end;
C4=[cA3',gcy3,gcy2,gcy1];
W4= waverec(C4,L,'db2');
hPs0=sum(s.^2);%信噪比signal power
hPn1=sum((s-s1).^2);
snr1=10*(log10(hPs0/hPn1));
hPn2=sum((s-h1).^2);
snr2=10*log10(hPs0/hPn2);
hPn3=sum((s-W').^2);
snr3=10*log10(hPs0/hPn3);
hPn4=sum((s-W3').^2);
snr4=10*log10(hPs0/hPn4);
hPn5=sum((s-W4').^2);
snr5=10*log10(hPs0/hPn5);
RMS1=sum((s-s1).^2)/ls;
RMS2=sum((s-h1).^2)/ls;
RMS3=sum((s-W').^2)/ls;
RMS4=sum((s-W3').^2)/ls;
RMS5=sum((s-W4').^2)/ls;
subplot(3,2,1);plot(s);title('某人一卡通消费')%信号图
subplot(3,2,2);plot(s1);title('使用软阈值去噪后的消费') 
subplot(3,2,3);plot(h1);title('使用硬阈值去噪后的消费') 
subplot(3,2,4);plot(W);title('文献9的阈值函数去噪后的消费') 
subplot(3,2,5);plot(W3);title('文献10的阈值函数去噪后的消费')
subplot(3,2,6);plot(W4);title('新阈值函数去噪后的消费')  
%输出结果
SNR = [snr1,snr2,snr3,snr4,snr5]
RMS = [RMS1,RMS2,RMS3,RMS4,RMS5]
