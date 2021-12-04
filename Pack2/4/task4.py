#! /usr/bin/python3

import time
import math

class IntervalToHTML:
    def __init__(self, func):
        self.func = func
    def __call__(self, args):
        self.func(args)
        print('<html><body>{}ms</body></html>'.format(self.func.gettime()))
# Декоратор
class TimeInterval:
    def __init__(self, func):
        self.func = func
    def __call__(self, args):
        start = time.perf_counter_ns()
        result = self.func(args)
        end = time.perf_counter_ns()
        self.interval = math.floor((end - start) / 1000000)
        return result
    def gettime(self):
        return self.interval
# Возведение в квадрат через цикл
@IntervalToHTML
@TimeInterval
def power2FOR(num_array):
    result = list()
    for i in num_array:
        result.append(num_array[i] * num_array[i])
    return result
# Возведение в квадрат через comprehension
@IntervalToHTML
@TimeInterval
def power2COM(num_array):
    return [i*i for i in num_array]
# Возведение в квадрат через map
@IntervalToHTML
@TimeInterval
def power2MAP(num_array):
    return list(map(lambda i: i*i, num_array))
    
if __name__ == "__main__":
    print("--------Task4--------")
    # Замеры времени исполнения
    array = list(range(10000001))
    print("FOR realization:")
    power2FOR(array)
    print("COMprehension realization:")
    power2COM(array)
    print("MAP realization:")
    power2MAP(array)
