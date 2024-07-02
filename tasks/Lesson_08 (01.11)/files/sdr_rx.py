import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt  

     
sdr = adi.Pluto("ip:192.168.2.1")   
table = 8   
sdr.rx_lo = 2000000000 + 2000000 * table   
#sdr.tx_lo = 2000000000 + 2000000 * table   
sdr.sample_rate = 1e6   
sdr.rx_buffer_size = 10000   
#samples = np.ones(sym_length * len(bits), dtype=complex)  

"""
for r in range(1): 
    rx = sdr.rx()    
    #plt.plot(big_array)   
    #plt.plot(rx.imag)  
    plt.clf()  
    plt.plot(abs(rx))    
    plt.draw() 
    plt.pause(0.05) 
    time.sleep(0.1) 
plt.show()
"""
bits = (24, [])
array = abs(sdr.rx())
#plt.plot(array)
#plt.show()
count = 0
print("!!!")
for i in range (len(array)):
    if array[i] > 1500:
    	count += 1
    elif array[i] < 500:
    	count = 0
    if(count == 16*100):
    	print("URAAAAAAAAAAAAAAA")
    	count = 0
    	print("index sync end = ", i)
    	array2 = array[(i- 16*100 - 1):i+2000]
    	print(len(array2))
    	plt.plot(array2)
    	plt.show()
    	time.sleep(100)
    	
print(bits)
    			
    			