#! /usr/bin/python3
import time
import math
if __name__ == "__main__":
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
    @TimeInterval
    def power2FOR(num_array):
        result = list()
        for i in num_array:
            result.append(num_array[i] * num_array[i])
        return result
    # Возведение в квадрат через comprehension
    @TimeInterval
    def power2COM(num_array):
        return [i*i for i in num_array]
    # Возведение в квадрат через map
    @TimeInterval
    def power2MAP(num_array):
        return list(map(lambda i: i*i, num_array))
    # Замеры времени исполнения
    array = list(range(10000001))
    print("FOR realization:")
    power2FOR(array)
    print("COMprehension realization:")
    power2COM(array)
    print("MAP realization:")
    power2MAP(array)
