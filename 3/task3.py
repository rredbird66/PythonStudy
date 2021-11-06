#! /usr/bin/python3
elements_array = ["a", "b", "c"]
print("--------Task3--------")
print("Raw data:", elements_array)
def enumerated(data):
    return list(zip(range(len(data)), data))
print("Enumerated:", enumerated(elements_array))
