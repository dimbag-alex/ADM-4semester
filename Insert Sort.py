import time
import random

def time_counter(func):
    def wraper(args):
        now = time.perf_counter()
        x = func(args)
        newnow = time.perf_counter()
        print(f"Функция  сработала за {newnow - now} секунды")
        return x
    return wraper


#s = [1000000, 1000000, 59, 29, 32, 23, 1, -1, 9, 19, 17, 31, 23, 46, 92, -1, -1, -1, -1, -1, 1000000]


# s = [3, 5, 1, 2, 4]
@time_counter
def insert_sort(s):
    for i in range(1, len(s)):
        x = s[i]
        j = i - 1
        while j >= 0 and s[j] > x:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = x
    return s


#s = random.randint(1, 1000000,)
# s = [3, 5, 1, 2, 4]
s = [random.randint(-1000, 1000) for _ in range(10000)]
#print(s)
print(insert_sort(s))
