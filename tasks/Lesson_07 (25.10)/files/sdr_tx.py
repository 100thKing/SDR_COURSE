import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt   
     
sdr = adi.Pluto("ip:192.168.2.1")   
table = 8   
##sdr.rx_lo = 2452000000 + 2000000 * table 
sdr.tx_lo = 2100000000 + 2000000 * table  
sdr.sample_rate = 1e6   
##sdr.rx_rf_bandwidth = sdr.sample_rate 
##sdr.rx_buffer_size = 10000   
sdr.tx_hardwaregain_chan0 = -10 #рекомендуемое значение от 0 до -50 
fc = 1000 
ts = 1/float(sdr.sample_rate) 
t = np.arange(0, 20000, ts) #fc*ts
i = np.cos(2 * np.pi * t * fc) * 2 ** 14 
q = np.sin(2 * np.pi * t * fc) * 2 ** 14 
samples = i + 1j * q 
  
#destroy buffer 
sdr.tx_destroy_buffer() 
 
# Start the transmitter 
sdr.tx_cyclic_buffer = True # Enable cyclic buffers 
sdr.tx(samples)
