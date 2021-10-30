import time
import math

print("--------Task5--------")
# Декоратор
def TimeInterval(func):
    def Wrapper(arg):
        time_stamp = time.perf_counter_ns()
        result = func(arg)
        print("Function execution time:", math.floor((time.perf_counter_ns() - time_stamp) / 1000000), "ms")
        return result
    return Wrapper
# Возведение в квадрат через цикл
def power2FOR(num_array):
    result = list()
    for i in num_array:
        result.append(num_array[i] * num_array[i])
    return result
# Возведение в квадрат через comprehension
def power2COM(num_array):
    return [i*i for i in num_array]
# Возведение в квадрат через map
def power2(number):
    return number*number
def power2MAP(num_array):
    return list(map(power2, num_array))
# Замеры времени исполнения
array = list()
for i in range(10000001):
    array.append(i)
timeFOR = TimeInterval(power2FOR)
timeCOM = TimeInterval(power2COM)
timeMAP = TimeInterval(power2MAP)
print("FOR realization:")
timeFOR(array)
print("COMprehension realization:")
timeCOM(array)
print("MAP realization:")
timeMAP(array)
