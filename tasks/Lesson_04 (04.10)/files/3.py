# -*- coding: utf-8 -*-

from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt


fc=20 # Частота косинуса 
fs=32*fc
t=np.arange( 0, 2,  1/fs) # длительность сигнала 2 с
x=np.cos(2*np.pi*fc*t) # формирование временного сигнала

plt.figure(1)
plt.plot(t,x) 
#plt.stem(t,x) # для отображения временных отсчетов сигнала, выбрать длительность 0.2 сек
plt.xlabel('$t=nT_s$')
plt.ylabel('$x[n]$') 
N=256 # количество точек ДПФ
X = fft(x,N)/N # вычисление ДПФ и нормирование на N

plt.figure(2)
k = np.arange(0, N)
plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
plt.xlabel('k')
plt.ylabel('$x[k]$') 

df=fs/N
kf = k*df
plt.figure(3)
plt.stem(kf,abs(X)) # выводим модуль ДПФ в частотах 
plt.xlabel('Гц')
plt.ylabel('$x[k]$') 