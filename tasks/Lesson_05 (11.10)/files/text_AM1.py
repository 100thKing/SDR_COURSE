
from scipy.fftpack import fft, ifft,  fftshift, ifftshift
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
import numpy as np
import matplotlib.pyplot as plt

 
Ns = 2048 # количество дискретных отсчетов сигнала
Tmax = 10 # временной интервал формирования сигнала
dt=Tmax/(Ns-1)  # интервал дискретизации
fs = 1/dt #частота дисктеризации 
t=np.arange(0, 10,1/fs) 

Ac = 2   #амплитуда несущего колебания
fc = 4  #частота несущего колебания
wc = 2*np.pi*fc
xc = np.cos(wc*t) # Несущее колебание f=4

Am = 1 #амплитуда НЧ колебания
fm = 0.5  # Частота НЧ несущего колебания
wm = 2*np.pi*fm # модулирующий НЧ сигнал f=0.5
xm = np.cos(wm*t) # НЧ сигнал

mu = Am/Ac #коэффициент модуляции
 
sam = Ac*(1+mu*xm)*xc # АМ сигнал 
plt.figure(1)
plt.plot(t,xm) #sam
plt.title('НЧ сигнал')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$') 


N=2048 # количество точек ДПФ
X = fft(xm,N)/N # вычисление ДПФ и нормирование на N ####
plt.figure(2)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр НЧ сигнала')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$') 



s_d = sam**2 # квадратичный детектор, возводим принятое колебание в 2
plt.figure(3)
plt.plot(t,s_d)
plt.title('Колебание АМ при квадратичном детектировании')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$') 


Xd = fft(s_d)/N # вычисление ДПФ и нормирование на N
plt.figure(4)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(Xd[0:100 ]  )) # спектр сигнала после возведения в 2
plt.title('Спектр колебания АМ при кв.дет. ')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$') 


n=99
fn =   fm/fs
taps=signal.firwin(n,fn) # вычисляем ИХ ФНЧ с нормированной частотой 
d=2*signal.lfilter(taps,1.0,s_d) # сигнал на выходе ФНЧ (выход детектора)
plt.figure(5)
plt.plot(t,d)
plt.title('Сигнал на выходе ФНЧ детектора ')
plt.xlabel('t')
plt.ylabel('$m(t)$') 


Xdd = fft(d)/N # вычисление ДПФ и нормирование на N
plt.figure(6)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100]  ,abs(Xdd[0:100] )) 
plt.title('Спектр сигнала на выходе ФНЧ детектора ')
plt.xlabel('f')
plt.ylabel('$m(f)$') 

plt.figure(7)
plt.plot(t,xc) #sam
plt.title('Несущий сигнал')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$') 


X = fft(xc,N)/N # вычисление ДПФ и нормирование на N ####
plt.figure(8)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр несущего сигнала')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$')