import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt   
  
Ns = 100   
bits = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   
                 0,1,1,1,0,0,1,1,0,1,1, 
                 1,1,1,1,1,1,1,1,1,1,1])   
  
                   
sdr = adi.Pluto("ip:192.168.2.1")   
sdr.rx_lo = 900000000 
sdr.tx_lo = 900000000 
sdr.sample_rate = 1e6   
sdr.rx_buffer_size = 100000   
 
#Генерируем QPSK-модулированный сигнал, 16 сэмплов на символ 
x_symbols = [] 
for i in range(len(bits)): 
    if bits[i] == 1: 
        x_symbols.append(1/np.sqrt(2) + 1j*1/np.sqrt(2)) 
    else: 
        x_symbols.append(-1/np.sqrt(2) - 1j*1/np.sqrt(2)) 
samples = np.repeat(x_symbols, Ns) # ns сэмплов на символ 
samples *= 2**14 #Повысим значения для наших сэмплов 
 
  
# Start the transmitter 
sdr.tx_cyclic_buffer = True # Enable cyclic buffers 
sdr.tx(samples) 
rx = sdr.rx 
 
plt.figure(1) 
plt.scatter(rx.real, rx.imag) 
 
plt.figure(2) 
plt.plot(rx.real, rx.imag) 
 
plt.show()
