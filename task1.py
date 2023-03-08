#Помогаев Максим R3142, 2 вариант
import time
import random
import numpy as np

first_list = [random.randint(1, 100) for i in range(1000001)]
second_list = [random.randint(1, 100) for i in range(1000001)]

time_start_lists = time.perf_counter()
for i in range(1000001):
    first_list[i] * second_list[i]
all_time_lists = time.perf_counter() - time_start_lists
print(all_time_lists)

first_array = np.array(first_list, int)
second_array = np.array(second_list, int)

time_start_arrays = time.perf_counter()
np.multiply(first_array, second_array)
all_time_arrays = time.perf_counter() - time_start_arrays
print(all_time_arrays)
