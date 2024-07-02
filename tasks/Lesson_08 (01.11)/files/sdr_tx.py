import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt   
  
  
sym_length = 100   
bits = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   
                 0,1,1,1,0,0,1,1,   
                 0,1,1,0,1,1,1,1,   
                 0,1,1,1,0,0,1,1,  
                 1,1,1,1,1,1,1,1,1,1,1])   
  
                   
sdr = adi.Pluto("ip:192.168.3.1")   
table = 8   
#sdr.rx_lo = 2000000000 + 2000000 * table   
sdr.tx_lo = 2000000000 + 2000000 * table   
sdr.sample_rate = 1e6   
sdr.rx_buffer_size = 100000   
samples = np.ones(sym_length * len(bits), dtype=complex)  
   
for i in range(len(bits)):   
    if (bits[i] == 1):   
        for j in range(i*sym_length, i*sym_length+sym_length):   
            samples[j] = ( 1 * 2**13 + 1j * 2**13 )  
    else:   
        for j in range(i*sym_length, i*sym_length+sym_length):   
            samples[j] =  (1 * 10 + 1j * 10 )  
big_array = np.array([])  
#sdr.tx_cyclic_buffer = True  
#sdr.tx_hardwaregain_chan0 = 0 #рекомендуемое значение от 0 до -50 
#tx = sdr.tx()
for r in range(100):   
    if(r >= 20 or r <= 30):   
      sdr.tx(samples)  
    #rx = sdr.rx()   
    #big_array = np.concatenate([big_array, abs(rx)])   
   
#plt.plot(big_array)   
plt.plot(samples)   
#plt.plot(abs(rx))   
#plt.show()