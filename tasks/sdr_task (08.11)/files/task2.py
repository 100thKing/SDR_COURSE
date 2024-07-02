from scipy.fftpack import fft, ifft,  fftshift, ifftshift 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
fc=20 # Частота косинуса  
fs=320*fc # частота дискретизации 
fs2=400 # частота дискретизации для второго сигнала
t=np.arange( 0, 0.03 , 1/fs) # длительность сигнала 0.03 с 
x=np.cos(2*np.pi*fc*t)# формирование временного сигнала
x2 = np.cos(2 * np.pi * 25 * t) + np.cos(6 * np.pi * 50 * t) 
N = 512 
 
plt.figure(1)  
plt.stem(t,x) 
 
xn1 = x[:64] 
xn2 = x[:128] 
xn3 = x[:256] 
 
plt.figure(2) 
plt.stem(xn1) 
 
plt.figure(3) 
plt.stem(xn2) 
 
plt.figure(4) 
plt.stem(xn3) 
 

fc1 = (0.1*np.pi*fs)/(2*np.pi) # определение значение аналоговой частоты сигнала
fc2 = (0.3*np.pi*fs)/(2*np.pi) 
print(fc1, " ", fc2)

plt.figure(5) # ДПФ сигнала
X1 = fft(xn1,N)/N 
k = np.arange(0, N) 
plt.stem(k,abs(X1)) 
plt.xlabel("Гц") 

plt.figure(6) # ДПФ сигнала
X2 = fft(xn2,N)/N 
k = np.arange(0, N) 
plt.stem(k,abs(X2)) 
plt.xlabel("Гц") 
 
plt.figure(7) # ДПФ сигнала
X3 = fft(xn3,N)/N 
k = np.arange(0, N) 
plt.stem(k,abs(X3)) 
plt.xlabel("Гц") 
 
plt.figure(8) 
spec= fft(x2) # спектр ДПФ суммы двух гармонических колебаний
plt.stem(t,abs(spec))

