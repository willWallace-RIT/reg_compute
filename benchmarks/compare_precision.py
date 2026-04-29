import time
import random

def full_precision(x):
    return (x ** 2) + (x * 0.5)

def low_precision(x):
    return (x * x)

data = [random.uniform(0, 1000) for _ in range(100000)]

start = time.time()
_ = [full_precision(x) for x in data]
print("Full:", time.time() - start)

start = time.time()
_ = [low_precision(int(x)) for x in data]
print("Low:", time.time() - start)
