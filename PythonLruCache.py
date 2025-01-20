import time
from functools import lru_cache

@lru_cache(maxsize=32)
def cacheFunc(num):
    #COMPLETE CODE HERE SO<1 2 3 4 5 6>
    time.sleep(num)
    return num

if __name__ == '__main__':
    print("Cache Function is running now")
    cacheFunc(3)
    print("Cache function is running now again")
    cacheFunc(2)
    print("Cache Function runned")

