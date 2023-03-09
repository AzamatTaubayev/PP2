import math
import time

def my4(n, ms):
    print(time.time())
    time.sleep(ms/1000)
    print(f'Square root of {n} after {ms} miliseconds is {math.sqrt(n)}')
    print(time.time())

my4(int(input()), int(input()))