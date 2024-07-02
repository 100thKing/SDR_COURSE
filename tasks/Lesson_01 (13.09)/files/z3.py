import numpy as np
import matplotlib.pyplot as plt

# массив значений 
t = np.arange(0, 10, 0.01)


A = 1
f = 1
phi = np.pi / 4.0

# значения синусоиды
y1 = A * np.sin(2 * np.pi * f * t + phi)
# cos
y2 = A * np.cos(2 * np.pi * f * t + phi)

# Создание графика
plt.figure(figsize=[8, 4])


plt.step(t, y1, label ='sin')
plt.plot(t, y2, label ='cos')

plt.xlabel('Time')
plt.ylabel('Amplitude')

# заголовок к графику 
plt.title('A * sin(w*f*t)/A * cos(w*f*t)') 

plt.legend()
plt.grid(True)

#plt.show()


