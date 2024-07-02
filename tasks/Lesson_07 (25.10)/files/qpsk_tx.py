import time   
import adi   
import numpy as np   
import matplotlib.pyplot as plt   
     
sdr = adi.Pluto("ip:192.168.3.1")   
table = 8   
# sdr.rx_lo = 2000000000
sdr.tx_lo = 2000000000  
sdr.sample_rate = 1e6   
# sdr.rx_rf_bandwidth = sdr.sample_rate 
# sdr.rx_buffer_size = 10000   
sdr.tx_hardwaregain_chan0 = 0 #рекомендуемое значение от 0 до -50 
 
#Генерируем QPSK-модулированный сигнал, 16 сэмплов на символ 
num_symbols = 1000 
x_int = np.random.randint(0, 4, num_symbols) # 0 to 3 
x_symbols = []
for i in range(len(x_int)):
    if x_int[i] == 0:
        x_symbols.append(1/np.sqrt(2) + 1j*1/np.sqrt(2))
    elif x_int[i] == 1:
        x_symbols.append(1/np.sqrt(2) - 1j*1/np.sqrt(2))
    elif x_int[i] == 2:
        x_symbols.append(-1/np.sqrt(2) - 1j*1/np.sqrt(2))
    elif x_int[i] == 3:
        x_symbols.append(-1/np.sqrt(2) + 1j*1/np.sqrt(2))

#print(x_int)
#print(x_symbols)

#= np.cos(x_radians) + 1j*np.sin(x_radians) #генерируем комплексные числа 
samples = np.repeat(x_symbols, 16) # 16 сэмплов на символ 
samples *= 2**10 #Повысим значения для наших сэмплов 
plt.figure(1)
plt.plot(samples.real)
plt.show()
#destroy buffer 
sdr.tx_destroy_buffer() 
 
#Start the transmitter 
sdr.tx_cyclic_buffer = True # Enable cyclic buffers 
sdr.tx(samples) 
psd = np.abs(np.fft.fftshift(np.fft.fft(samples)))**2
psd_dB = 10*np.log10(psd)
f = np.linspace(sdr.sample_rate/-2, sdr.sample_rate/2, len(psd))
plt.plot(f/1e6, psd_dB)
plt.xlabel("Частота [MHz]")
plt.ylabel("PSD")
plt.show()
 
# rx = sdr.rx() 
# plt.figure(1)
# plt.scatter(rx.real, rx.imag)
# plt.figure(2)
# plt.plot(rx.real)
# plt.show()