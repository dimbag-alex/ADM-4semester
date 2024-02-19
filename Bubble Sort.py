# сортировка пузырьком
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
def bubblesort(s):
    temp = 0
    for j in range(len(s) - 1, 0, -1):
        for i in range(0, j):
            if s[i] > s[i + 1]:
                #s[i], s[i + 1] = s[i + 1], s[i]
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp

    return s


s = [random.randint(-1000, 1000) for _ in range(10000)]
print(bubblesort(s) == sorted(s))

