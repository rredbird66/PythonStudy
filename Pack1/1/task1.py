#! /usr/bin/python3
if __name__ == "__main__":
    names = ["python", "perl", "java", "c", "haskell", "ruby"]
    print("--------Task1--------")
    print("Raw data:", names)
    def lensort(data):
        print("Sorted data:",sorted(data, key = len))
    lensort(names)
    print("Raw data after lensort(data):", names)
