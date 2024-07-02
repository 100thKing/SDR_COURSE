import time 
import random
import numpy as np
import matplotlib.pyplot as plt



# списки для хранения времени сортировки
list_times = []
numpy_times = []


element_counts = list(range(100000, 5000000, 150000))

for count in element_counts:
    # случайный массив данных для сортировки
    data = np.random.rand(count)

    # время сортировки для списка Python
    start_time = time.time()
    sorted_list = sorted(data)
    list_time = time.time() - start_time
    list_times.append(list_time)

    # время сортировки для NumPy
    start_time = time.time()
    sorted_numpy = np.sort(data)
    numpy_time = time.time() - start_time
    numpy_times.append(numpy_time)

# построение графика
plt.plot(element_counts, list_times, label='Python Lists')
plt.plot(element_counts, numpy_times, label='NumPy')
plt.xlabel('Количество элементов')
plt.ylabel('Время выполнения, с')
plt.title('Сравнение времени сортировки Python Lists и NumPy')
plt.legend()
plt.grid(True)
plt.show()





