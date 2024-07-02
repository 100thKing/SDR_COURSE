import numpy as np
import matplotlib.pyplot as plt

# массив значений 
t = np.arange(0, 10, 0.01)
A = 1
f = 1
phi = np.pi / 4.0
y1 = A * np.sin(2 * np.pi * f * t + phi)

#  объект Figure и массив объектов Axes
fig, axes = plt.subplots(3, 1, figsize=(6, 8))

# первый график (Аналоговый)
axes[0].plot(t, y1)
axes[0].set_title('Аналоговый')
axes[0].set_xlabel('Время')
axes[0].set_ylabel('Амплитуда')
axes[0].grid(True)

# второй график (Квантованный)
axes[1].step(t, y1)
axes[1].set_title('Квантованный')
axes[1].set_xlabel('Время')
axes[1].set_ylabel('Уровень')
axes[1].grid(True)

# третий график (Дискретный)
axes[2].stem(t, y1)
axes[2].set_title('Дискретный')
axes[2].set_xlabel('Время')
axes[2].set_ylabel('Уровень')
axes[2].grid(True)


fig.suptitle('Сравнение стилей отображения')
plt.tight_layout()
plt.show()
