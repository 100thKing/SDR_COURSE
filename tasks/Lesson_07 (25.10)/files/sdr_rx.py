import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt   
     
sdr = adi.Pluto("ip:192.168.3.1")   
table = 8   
sdr.rx_lo = 2100000000 + 2000000 * table  
sdr.sample_rate = 1e6   
sdr.rx_rf_bandwidth = sdr.sample_rate 
sdr.rx_buffer_size = 10000   
sdr.rx_hardwaregain_chan0 = 10


 
for r in range(60): 
    rx = sdr.rx() 
    plt.clf() 
    plt.plot(rx.real) 
    plt.plot(rx.imag) 
    plt.ylim([-2000, 2000]) 
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()
