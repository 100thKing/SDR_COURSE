import time 
import adi 
import matplotlib.pyplot as plt 
import numpy as np 
 
# Используем элементы библиотеки для вывода 
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 
 
# Create radio 
sdr = adi.Pluto("ip:192.168.3.1") 
 
# Configure properties 
sdr.rx_lo = 2452000000 
 
# Collect data 
for r in range(60): 
    rx = sdr.rx() 
    N=1024 
    X = fft(rx,N)/N 
    plt.figure("FFT") 
    plt.clf() 
    plt.stem(abs(X)) 
    plt.ylim([0, 2000]) 
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()

