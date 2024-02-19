#сортировка расческой
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
@time_counter


def combsort(s):
    divider = 1.247
    n = len(s) / divider
    while n > 1:
        nrounded = round(n)
        for j in range(0, len(s) - nrounded):
            if s[j] > s[j + nrounded]:
                s[j], s[j + nrounded] = s[j + nrounded], s[j]
        n /= divider
    return s

#s = [random.randint(-1000000, 1000000) for _ in range(10000)]
s = [random.randint(-1000000000, 1000000000) for _ in range(random.randint(1, 1000000000))]
print(combsort(s) == sorted(s))
