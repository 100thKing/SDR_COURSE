from scipy.fftpack import fft, ifft,  fftshift, ifftshift
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x=np.array([1,1,1,-1,1]) #код Баркера из 5 значений
#x = np.array([+1, +1, +1, -1, -1, -1, +1, -1, -1, +1, -1]) # код Баркера из 11 значений
y=np.correlate(x,x,"full")
plt.plot(y)
plt.show() 