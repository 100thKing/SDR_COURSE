import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt  
from scipy.fftpack import fft, ifft, fftshift
     
sdr = adi.Pluto("ip:192.168.3.1")   
table = 8   
sdr.rx_lo = int(800e6)
sdr.sample_rate = 1e6   
sdr.rx_rf_bandwidth = sdr.sample_rate 
sdr.rx_buffer_size = 10000 
sdr.rx_hardwaregain_chan0 = 50


 
while 1: 
    rx = sdr.rx() 
    N = 1024
    X = fft(rx,N)/N
    plt.figure("FFT")
    plt.clf()  
    plt.stem() 
    plt.ylim([-2000, 2000]) 
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()
