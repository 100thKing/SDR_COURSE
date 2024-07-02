from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import max_len_seq
import adi

ft= 100e3  # символьная скорость (частота следования символов)
fs = 600e3  # частота дискретизации
ns = fs/ft # кол-во отсчетов на символ (примерно 6)
data=max_len_seq(6)[0]
print(data)
b = np.ones(int(ns)) #Коэффициенты фильтра интерполятора
m=2*data-1
ts1 =np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1]) # длина заголовка 26
ts1t = 2*ts1-1
print(ts1t)
#print(m)
x_IQ = m

#x_IQ = np.hstack((ts1t,m)) # формирование пакета 
 
N_input = len(x_IQ)
xup = np.hstack((x_IQ.reshape(N_input,1),np.zeros((N_input, int(ns-1))))) # матрица
xup= xup.flatten()
#print(xup)

x1 = signal.lfilter(b, 1,xup)
x=x1.astype(complex)
x1 = signal.lfilter(b, 1,xup)
x=x1.astype(complex)
b = np.ones(int(ns)) #Коэффициенты фильтра интерполятора
xt=.5*(1+x) #комплексные отсчеты для adalm
#print(xt)
triq=2**14*xt
n_frame= len(triq)

sdr = adi.Pluto("ip:192.168.2.1")  
  
# Configure properties  
sdr.rx_lo = 2452000000
sdr.tx_lo = 2452000000
sdr.rx_rf_bandwidth = 200000 
sdr.rx_destroy_buffer() 
sdr.tx_hardwaregain_chan0 = -10 
sdr.rx_buffer_size = 2*n_frame 
xrec1=sdr.rx() 
xrec = xrec1/np.mean(xrec1**2) 
 

#destroy buffer  


# код Баркера
# x=np.array([1,1,1,-1,1])
# y=np.correlate(x,x,"full")
# plt.plot(y)
# plt.show() ctrl kc