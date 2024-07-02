import adi
import numpy as np
import matplotlib.pyplot as plt
import time
sdr = adi.Pluto("ip:192.168.2.1")
sdr.rx_lo = 2000000000
sdr.sample_rate = 1e6   
sdr.rx_hardwaregain_chan0 = 50
sdr.rx_rf_bandwidth = sdr.sample_rate 
sdr.rx_buffer_size = 10000
while True:
    rx = sdr.rx() 
    plt.figure(1)
    plt.clf()
    plt.scatter(rx.real, rx.imag)
    plt.draw()
    plt.figure(2)
    plt.clf()
    plt.plot(rx.real)
    plt.draw()
    plt.pause(0.05)
    # time.sleep(0.1)