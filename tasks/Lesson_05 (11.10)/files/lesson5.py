import time 
import adi 
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 
from scipy import signal 
from scipy.signal import kaiserord, lfilter, firwin, freqz 
import numpy as np 
import matplotlib.pyplot as plt 
 
sdr = adi.Pluto("ip:192.168.3.1") 
table = 8 
sdr.rx_lo = 2452000000 + 2000000 * table 
sdr.tx_lo = 2452000000 + 2000000 * table 
sdr.sample_rate = 1e6 
N = 1024 
 
fc = 10000 
ts = 1/float(sdr.sample_rate) 
t = np.arange(0, fc*ts, ts) 
i = np.sin(2*np.pi*t*fc) * 2**14 
q = np.cos(2*np.pi*t*fc) * 2**14 
samples = i + 1j*q 
 
#destroy buffer 
sdr.tx_destroy_buffer() 
 
# Start the transmitter 
sdr.tx_cyclic_buffer = True # Enable cyclic buffers 
sdr.tx(samples) 
 
for r in range(60): 
    rx = sdr.rx() 
    plt.clf() 
    plt.plot(rx.real) 
    plt.plot(rx.imag) #######
    plt.ylim([-2000, 2000]) 
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()


